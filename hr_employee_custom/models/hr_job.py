from odoo import models, fields, api
from odoo.osv import expression

class HrJob(models.Model):
    _inherit = 'hr.job'

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
        required=True
    )

    @api.onchange('department_id')
    def _onchange_department_id_set_company(self):
        if self.department_id and self.department_id.company_id:
            self.company_id = self.department_id.company_id

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('company_id') and vals.get('department_id'):
                dept = self.env['hr.department'].browse(vals['department_id'])
                if dept.company_id:
                    vals['company_id'] = dept.company_id.id
            if not vals.get('company_id'):
                vals['company_id'] = self.env.company.id
        return super(HrJob, self).create(vals_list)

    @api.model
    def _name_search(self, name='', domain=None, operator='ilike', limit=100, order=None):
        domain = domain or []
        target_company_id = self.env.context.get('company_id') or self.env.company.id

        if name and target_company_id:
            # 1. Search specifically in current active company
            comp_domain = expression.AND([
                domain,
                [('name', operator, name), ('company_id', '=', target_company_id)]
            ])
            comp_results = self._search(comp_domain, limit=limit, order=order)
            if comp_results:
                return comp_results

            # 2. Search in global (no company set)
            global_domain = expression.AND([
                domain,
                [('name', operator, name), ('company_id', '=', False)]
            ])
            global_results = self._search(global_domain, limit=limit, order=order)
            if global_results:
                return global_results

        return super(HrJob, self)._name_search(name=name, domain=domain, operator=operator, limit=limit, order=order)

    def _auto_init(self):
        res = super(HrJob, self)._auto_init()
        # Backfill company_id for existing job positions from their department if missing
        self.env.cr.execute("""
            UPDATE hr_job j
            SET company_id = d.company_id
            FROM hr_department d
            WHERE j.department_id = d.id
              AND j.company_id IS NULL
              AND d.company_id IS NOT NULL;
        """)
        return res

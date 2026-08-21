from odoo import models, fields, api

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

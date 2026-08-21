from odoo import models, api
from odoo.osv import expression

class HrDepartment(models.Model):
    _inherit = 'hr.department'

    @api.model
    def _name_search(self, name='', domain=None, operator='ilike', limit=100, order=None):
        domain = domain or []
        target_company_id = self.env.context.get('company_id') or self.env.company.id

        if name and target_company_id:
            comp_domain = expression.AND([
                domain,
                [('name', operator, name), ('company_id', '=', target_company_id)]
            ])
            comp_results = self._search(comp_domain, limit=limit, order=order)
            if comp_results:
                return comp_results

        return super(HrDepartment, self)._name_search(name=name, domain=domain, operator=operator, limit=limit, order=order)

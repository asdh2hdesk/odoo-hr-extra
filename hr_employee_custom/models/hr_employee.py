from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    father_name = fields.Char(required=True)
    department_id = fields.Many2one(
        'hr.department',
        required=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]"
    )
    job_id = fields.Many2one(
        'hr.job',
        required=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]"
    )
    employee_code = fields.Char(required=True)

   
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    father_name = fields.Char(required=True)
    department_id = fields.Many2one('hr.department', required=True)
    job_id = fields.Many2one('hr.job', required=True)
    employee_code = fields.Char(required=True)

   
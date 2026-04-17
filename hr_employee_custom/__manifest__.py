{
    'name': 'Custom Employee Management',
    'version': '18.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Customizations for Employee Master',
    'author': 'Balaji Bathini',
    'depends': ['hr', 'hr_payroll', 'hr_employee_updation', 'hr_employee_entended', 'EHS', 'l10n_in_hr_payroll','custom_css_ui'],
    'data': [
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}

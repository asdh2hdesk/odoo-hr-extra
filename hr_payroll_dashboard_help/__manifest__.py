# -*- coding: utf-8 -*-
{
    'name': 'HR Payroll Dashboard Help',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/Payroll',
    'summary': 'Adds a Help menu with the HR Process PPT inside the HR Payroll Dashboard app',
    'description': """
        Standalone add-on for the HR Payroll Dashboard app:
        - Adds a "Help" menu next to "Dashboard" in the HR Dashboard app bar.
        - Adds a "PPT" sub-menu under Help that opens the HR Process
          presentation in a new browser tab.
        - Does not modify any file of the hr_payroll_dashboard module.
    """,
    'author': 'vignesh',
    'website': 'https://yourcompany.com',
    'depends': ['base', 'hr_payroll_dashboard'],
    'data': [
        'views/hr_payroll_dashboard_help_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}

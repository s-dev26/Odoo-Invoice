# coding: utf-8
{
    'name': "S-DEV INVOICE CUSTOM",
    'summary': """
        S-DEV INVOICE""",
    'description': """
        Description de votre module""",
    'author': "S-DEV",
    'website': "https://www.s-dev.com",
    'category': 'Accounting',
    'version': '16.0',
    'license': 'LGPL-3',
    'depends': ['base', 'account'],
    'data': [
        'views/account_move_view.xml',
        'views/account_move_form.xml',
    ],
    'application': True,
    'icon': ''
}
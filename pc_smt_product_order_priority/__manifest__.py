# -*- coding: utf-8 -*-

{
    'name': 'Process SMT Producto default for report',
    'author': "ProcessControl",
    'version': '15.0.1.1',
    'summary': 'Process SMT Producto default for report',
    'description': """
            Process SMT Producto default for report
    """,
    'depends': ['base', 'sale'],
    'data': [
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'category': 'Accounting',
    'currency': "EUR",
}

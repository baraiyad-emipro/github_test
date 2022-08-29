# -*- coding: utf-8 -*-

{
    'name': 'Demo1',
    'version': '1.1',
    'author': 'Emipro Technologies Pvt. Ltd.',
    'category': 'Utility',
    'description': """
This module for demonstration of basic module.
    """,
    'website': 'http://www.emiprotechnologies.com',
    'depends': ['sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/partner_demo.xml',
    ],
    'demo': [
        'data/partner_demo_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

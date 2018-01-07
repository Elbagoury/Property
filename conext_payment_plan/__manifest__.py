# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Conext Payment Plan',
	'author': 'yoshin4g4@gmail.com',
	'website': 'http://conextsolution.com',
    'version': '1.1',
    'summary': 'Cicilan untuk Property',
    'description': """
Cicilan untuk Property
    """,

    'depends': ['conext_property','base','product','sales_team','account','sale'],
    'data': [
        'views/ir_sequence_data.xml',
        'views/payment_plan_view.xml',
        'views/account_invoice_view.xml',
        'views/account_payment_view.xml',
    ],
    'demo': [
    ],
    'css': [],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'auto_install': False,
}

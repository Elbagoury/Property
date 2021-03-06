# -*- coding: utf-8 -*-
{
    "name": "E-Faktur",
    "version": "1.0",
    'author': 'yoshin4g4@gmail.com',
    "description": """
    Change view for Indonesia
    """,
    "depends": ['account'],
    'init_xml': [],
    'update_xml': [
        'security/ir.model.access.csv',
        'views/faktur_pajak.xml',
        'views/invoice_inherit_view.xml',
        'wizard/generate_faktur_view.xml',
        'views/partner_sequence.xml',
		    'views/partner_view_inherit.xml',
    ],
    'css': [],
    'js': [
    ],
    'installable': True,
    'active': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

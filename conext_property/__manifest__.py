# -*- coding: utf-8 -*-
{
    'name': "Property Management",
    'version' : '1.1',
    'summary': """Property Management """,
    'sequence': 30,
    'description': """module untuk mengelola property
        
    """,

    'author': "yoshin4g4@gmail.com",
    'website': "http://conextsolution.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Property',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends' : ['base','account', 'sale', 'sale_stock', 'stock', 'purchase','sales_team'],

    # always loaded
    'data': [
        'views/property_unit.xml',
        'views/reserved.xml',
        'views/booking.xml',
        'views/property_sale.xml',
        'views/nota_kredit.xml',
#		'view/payment.xml',
        'views/iom.xml',
        'views/installment.xml',
        'views/estate_ipl.xml',
        'views/budget.xml',
        'views/material_req.xml',
        'sequence/sequence.xml',
        'menu.xml',
        'views/views.xml',
#      'views/ir_sequence_data.xml',
#      'views/payment_plan_view.xml',
#      'views/account_invoice_view.xml',
#      'views/account_payment_view.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

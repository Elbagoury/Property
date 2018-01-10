# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Demo Data Property',
    'version': '1.1',
    'category': 'Property',
    'description': """
Demo data Untuk Property Management""",
    'author': 'yoshin4g4',
    'website': 'http://conextsolution.com',
    'depends': ['conext_property','e_faktur'],
    'data': [
        'data/res.partner.csv',	
        'data/property.category.csv',
        'data/property.tower.csv',
        'data/property.jenis.csv',
        'data/property.type.csv',
        'data/property.view.csv',
		'data/property.floor.csv',
#		'data/product.template.csv',
    ],
    'demo' : [],
}

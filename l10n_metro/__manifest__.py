# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'COA Property',
    'version': '1.1',
    'category': 'Localization',
    'description': """
COA Untuk Property Management""",
    'author': 'yoshin4g4',
    'website': 'http://conextsolution.com',
    'depends': [ 'base', 'account','base_iban', 'base_vat'],
    'data': [
        'data/l10n_id_chart_data.xml',
        'data/account.account.template.csv',
        'data/account.chart.template.csv',
        'data/account.account.tag.csv',
        'data/account.tax.template.csv',
        'data/account_chart_template_data.yml',
    ],
    'demo' : [],
}

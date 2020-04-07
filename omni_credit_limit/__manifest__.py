# -*- coding: utf-8 -*-
{
    'name': "omni_customer_credit_limit",

    'summary': """
        Customer Credit Limit
    """,

    'description': """
        Credit Limit for Customer Accounts Receivable and Sales Orders
    """,

    'author': "OmniTechnical",
    'website': "https://omnitechnical.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','sale','contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}

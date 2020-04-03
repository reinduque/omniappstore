# -*- coding: utf-8 -*-
{
    'name': "omni_chart_of_accounts_ph",

    'summary': """
        OmniTechnical Chart of Accounts Philippines""",

    'description': """
        OmniTechnical Chart of Accounts Philippines
    """,

    'author': "OmniTechnical Global Solutions, Inc.",
    'website': "http://www.omnitechnical.com",

    # Categories can be used to filter modules in modules
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','account'],
    # always loaded
    'data': [
        # 'security/user_groups.xml',
        # 'security/security_data.xml',
        'views/views.xml',
        'data/chart_of_accounts_ph.xml',
        # 'views/templates.xml',
        

    ],
    'qweb': [
         # 'static/src/xml/extend_thread_fields.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

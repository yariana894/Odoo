# -*- coding: utf-8 -*-
{
    'name': "viajes",

    'summary': """
        Gestión de viajes""",

    'description': """
        Permite la gesntión de viajes
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'viajes, coches',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # es modelo
        'security/ir.model.access.csv',
        'views/vehiculo.xml',
        'views/viaje.xml',
        'views/partner.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

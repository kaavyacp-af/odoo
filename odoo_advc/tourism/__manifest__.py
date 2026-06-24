# -*- coding: utf-8 -*-
{
    'name': 'Tourism Management',
    'depends': ['base', 'sale', 'fleet'], 
    'application': True,
    'data': [
        "views/tourism_package_views.xml",
        "views/tourism_booking_views.xml",
        "views/tourism_package_type_views.xml",
        "views/tourism_package_tag_views.xml",
        "views/tourism_menus.xml",
        "views/res_users_views.xml",
        "security/ir.model.access.csv"
    ]
}
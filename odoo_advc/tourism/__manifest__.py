# -*- coding: utf-8 -*-
{
    'name': 'Tourism Management',
    'depends': ['base', 'sale', 'fleet'], 
    'application': True,
    'data': [
        "security/ir.model.access.csv",
        
        # Menus must be loaded BEFORE views that use them
        "views/tourism_menus.xml",
        
        # Then load the views
        "views/tourism_package_views.xml",
        "views/tourism_booking_views.xml",
        "views/tourism_package_type_views.xml",
        "views/tourism_package_tag_views.xml",
        "views/res_users_views.xml",
    ]
}
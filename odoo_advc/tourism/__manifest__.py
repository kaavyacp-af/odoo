{
    'name':'Tourism Management',
    'depends':['base', 'sale', 'fleet', 'website'],
    'application':True,
    'data' : [
        "views/tourism_package_views.xml",
        "views/tourism_booking_views.xml",
        "views/tourism_package_type_views.xml",
        "views/tourism_package_tag_views.xml",
        "views/tourism_menus.xml",
        "views/res_users_views.xml",
        "security/ir.model.access.csv",
        "views/tourism_package_templates.xml"
    ]
}
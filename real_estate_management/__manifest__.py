{
    'name': 'Real Estate Management',
    'version': '1.0',
    'summary': 'Module for managing real estate properties',
    'description': """
        Real Estate Management
        ======================
        This module helps in managing real estate properties, including property listings, sales, and rentals.
    """,
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
    'category': 'Real Estate',
    'depends': ['base'],
    'data': [
        # DATA
        'data/res_group.xml',
        'data/estate_property_category_data.xml',
        # SECURITY
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        # WIZARD
        'wizard/mass_edit_wizard.xml',
        # views
        'views/estate_property_views.xml',
        'views/estate_property_category_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/res_partner_views.xml',
        'views/menu.xml',
    ],
    'demo': [
        # List your demo files here
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
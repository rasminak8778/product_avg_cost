{
    'name': 'Product Average Cost',
    'version': '17.0.1.0.0',
    'description': 'Average Cost of All Products',
    'category': 'Purchase/Product Average Cost',
    'summary': 'Product Average Cost',
    'installable': True,
    'application': True,
    'depends': [
        'base',
        'purchase'
        ],
    'data': [
        'views/product_template_views.xml',
        'views/product_menu.xml'
    ]
}
# Copyright 2020 David Cantador - david.cantador@processcontrol.es
# License AGPL-3.0 or later
{
    "name": "Product Catalog Base",
    "summary":
        "Module to control the basic actions of the website catalog.",
    "version": "14.0.1.0.0",
    "category": "undefined",
    "website": "",
    "author": "ProcessControl",
    "license": "AGPL-3",
    "depends": [
        "base",
        "emipro_theme_base",
        "theme_clarico_vega",
        "project",
        "crm"
    ],
    'data': [
        'templates/assets.xml',
        'templates/product.xml',
        'templates/cart.xml',
        'views/product_template.xml'
    ],
    "application": True,
    "installable=": True
}

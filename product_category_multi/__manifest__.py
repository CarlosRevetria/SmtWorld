# coding: utf-8
{
    'name': 'Product Category Multi-Company',
    'version': '0.1',
    'category': 'inventory',
    'license': 'OPL-1',
    'price': 15.00,
    'images': ['static/description/company.png'],
    'author': 'oranga',
    'currency': 'EUR',
    'summary': 'Product Category Multi-Company',
    'description': """
Product Category Multicompany
Product Category Multi-Company
Product Category Multi company
""",
    "depends": [
        "product",
        "base"
    ],
    "data": [
        "security/security.xml",
        "view/product_category_view.xml"
    ],
    "installable": True,
    "auto_install": False,
}
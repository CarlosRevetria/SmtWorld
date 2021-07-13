# -*- coding: utf-8 -*-
# from odoo import http


# class ProductProductCustomImport(http.Controller):
#     @http.route('/product_product_custom_import/product_product_custom_import/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_product_custom_import/product_product_custom_import/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_product_custom_import.listing', {
#             'root': '/product_product_custom_import/product_product_custom_import',
#             'objects': http.request.env['product_product_custom_import.product_product_custom_import'].search([]),
#         })

#     @http.route('/product_product_custom_import/product_product_custom_import/objects/<model("product_product_custom_import.product_product_custom_import"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_product_custom_import.object', {
#             'object': obj
#         })

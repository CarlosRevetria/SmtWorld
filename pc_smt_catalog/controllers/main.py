from werkzeug import urls

from odoo import fields as odoo_fields, http, tools, _, SUPERUSER_ID
from odoo.exceptions import ValidationError, AccessError, MissingError, UserError, AccessDenied
from odoo.http import content_disposition, Controller, request, route
from odoo.tools import consteq
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.addons.website_sale.controllers.main import WebsiteSale
from datetime import datetime

import logging

# from odoo.addons.website_mass_mailing.controllers.main import MassMailController

_logger = logging.getLogger(__name__)


class WebsiteSale(WebsiteSale):
    @http.route(['/shop/payment'], type='http', auth="public", website=True, sitemap=False)
    def payment(self, **post):
        return request.redirect('/shop/cart')
    @http.route(['/shop/address'], type='http', auth="public", website=True, sitemap=False)
    def payment(self, **post):
        return request.redirect('/shop/cart')


class OppoForm(Controller):

    @route(['/my/oppo/new'], auth="public", type="http", website=True)
    def newOppo(self, redirect=None, **post):
        if post and request.httprequest.method == 'POST':
            sale_order = request.website.sale_get_order(force_create=True)
            if sale_order:
                valores = {}
                valores.update(post)

                if valores:
                    now = datetime.now()
                    date_time = now.strftime("%d/%m/%Y - %H:%M:%S")
                    website_name = request.website.name

                    crm_lead = request.env['crm.lead'].sudo().create({
                        'name': "New mstech website opportunity " + date_time,
                        'user_id': 10,
                        'team_id': 2
                    })
                    if crm_lead:
                        message_cart = "CONFIGURED PRODUCTS <br/><br/>"
                        i = 0

                        if sale_order.order_line:
                            for line in sale_order.order_line:
                                breaker = ""
                                if i > 0:
                                    breaker = "<br/>"
                                message_cart = message_cart + breaker + "Producto: " + line.product_id.name + " - Qty: " + str(
                                    line.product_uom_qty) + "<br/>"

                                i = i + 1
                            message_cart = message_cart + "-----------------------------------------"
                        message = message_cart + "<br/>Tell us about current throughput in your production: <br/>" \
                                                 "1. Number of products required in production per year: " + valores.get(
                            'products_required') + "<br/>" \
                                                   "2. Required cycle-time per board: " + valores.get(
                            'cycle_time') + "<br/>" \
                                            "3. Number of production shifts: " + valores.get(
                            'production_shifts') + "<br/>" \
                                                   "4. How many different types of boards?: " + valores.get(
                            'different_types') + "<br/><br/>" \
                                                 "Technical details: <br/>" \
                                                 "1. Description of the application and what are the customers objectives: " + valores.get(
                            'description_application') + "<br/>" \
                                                         "2. Board dimensions and carries dimensions containing how many boards: " + valores.get(
                            'board_dimensions') + "<br/>" \
                                                  "3. Material(s) types: " + valores.get('materials_types') + "<br/>" \
                                                                                                              "4. Types of Products that will be quoted: " + valores.get(
                            'types_products') + "<br/>" \
                                                "5. Geometry size. L/I/H mm: " + valores.get(
                            'geometry_size') + "<br/><br/>" \
                                               "Please tell us: <br/>" \
                                               "1. Estimated budget: " + valores.get('estimated_budget') + "<br/>" \
                                                                                                           "2. Estimated closing date: " + valores.get(
                            'estimated_closing_date') + "<br/><br/>" \
                                                        "Company details: <br/>" \
                                                        "Company Name: " + valores.get('company_name') + "<br/>" \
                                                        "Company Address: " + valores.get('company_address') + "<br/>" \
                                                        "Name / Surname: " + valores.get('name_surname') + "<br/>" \
                                                        "Email / Phone: " + valores.get('email_phone') + "<br/>"
                        crm_lead.sudo().message_post(body=message)
                    return request.redirect('/contactus-thank-you')
            else:
                # error
                raise UserError("")

        return request.redirect('/shop/cart')

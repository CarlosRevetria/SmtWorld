# Copyright 2021 David Cantador
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    url_tour_virtual = fields.Char(string='URL Tour Virtual (Youtube)', store=True)
    features_column_1 = fields.Html(string='Features Column 1', store=True)
    features_column_2 = fields.Html(string='Features Column 2', store=True)
    title = fields.Char(string='Titulo', store=True)
    short_description = fields.Text(string='Descripción Corta', store=True)
    long_description = fields.Text(string='Descripción Larga', store=True)
    measures = fields.Image("Measures", max_width=512, max_height=512, store=True)
    tech_details = fields.Html(string="Tech details", sanitize_attributes=True, strip_classes=False)
    benefits1 = fields.Image("Benefits 1", max_width=512, max_height=512, store=True)
    benefits2 = fields.Image("Benefits 2", max_width=512, max_height=512, store=True)
    benefits3 = fields.Image("Benefits 3", max_width=512, max_height=512, store=True)
    applications = fields.Text(string="Applications", store=True)

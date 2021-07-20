# coding: utf-8
from odoo import api, fields, models, tools, _

class ProductCategory(models.Model):
    _inherit = "product.category"

    company_id = fields.Many2one('res.company', string='Company', required=True,
                                     copy=False, default=lambda self: self.env['res.company']._company_default_get())
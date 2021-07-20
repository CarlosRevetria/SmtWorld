# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.


import base64
import io
from io import StringIO
from odoo import http, SUPERUSER_ID
from odoo.http import request
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.website_sale.controllers.main import WebsiteSale
import logging
_logger = logging.getLogger(__name__)

class WebsiteSaleAttachment(WebsiteSale):
    def _prepare_product_values(self, product, category, search, **kwargs):
        values = super(WebsiteSaleAttachment, self)._prepare_product_values(product, category, search, **kwargs)

        attachment_obj = request.env['product.attachment']
        attachments = attachment_obj.search([('product_tmpl_id', '=', product.id)])
        values['attachments'] = attachments
        return values

    @http.route(['/download/attachment'], type='http', auth="public", website=True)
    def download_attachment(self, attachment_id):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        attachment = request.env['product.attachment'].sudo().search_read([('id', '=', int(attachment_id))], ["attachment","file_name"])
        
        if attachment:
            attachment = attachment[0]
        else:
            return redirect('/shop')

        data = io.BytesIO(base64.standard_b64decode(attachment["attachment"]))
        return http.send_file(data, filename=attachment['file_name'], as_attachment=True)
    	    	
    	       
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:        

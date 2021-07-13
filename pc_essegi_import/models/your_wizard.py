# -*- coding: utf-8 -*-

import base64
import binascii
import codecs
import collections
import csv

import unicodedata

import chardet
import datetime
import io
import itertools
import logging
import psycopg2
import operator
import os
import re
import requests
from io import StringIO

from odoo import models, fields, api
from os.path import isfile, join, exists

_logger = logging.getLogger(__name__)
from odoo.exceptions import ValidationError
from collections import OrderedDict
import locale
from odoo.tools import config, DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, pycompat


class ESSEGI():
    def __init__(self, num_albaran, codigo_producto, cantidad):
        self.num_albaran = ""
        self.codigo_producto = ""
        self.cantidad = 0


class YourWizard(models.TransientModel):
    _name = 'your.wizard'

    csv_file = fields.Binary(string='CSV File', required=True)

    def import_csv(self):
        csv_data = base64.b64decode(self.csv_file).decode('utf-8')

        f = StringIO(csv_data)
        reader = csv.reader(f, delimiter=',')
        i = 0
        total_data = []

        for row in reader:
            if i > 1:
                for data in row:
                    line = data.split(",")
                    product_code = line[1]
                    if product_code:
                        product_code = product_code.replace("\"", "")
                    quantity = line[2]
                    if quantity:
                        quantity = float(quantity.replace("\"", ""))
                    albaran_prefix = line[10]
                    albaran_number = line[11]

                    albaran_complete = self._complete_albaran(albaran_prefix, albaran_number)

                    if product_code and quantity and albaran_complete:
                        stock_picking = self.env['stock.picking'].search([('name', '=', albaran_complete)])
                        if stock_picking:
                            stock_picking_lines = stock_picking.move_ids_without_package
                            if stock_picking_lines:
                                for line in stock_picking_lines:
                                    if line.product_id.default_code == product_code:
                                        line_id = line.id
                                        if line_id:
                                            line_data = self.env['stock.move'].browse(line_id)
                                            if line_data:
                                                line_data.write({
                                                    'quantity_done':  quantity
                                                })

            i = i + 1

    def _complete_albaran(self, code, number):
        res = False
        if code and number:
            res = str(code) + "/" + str(number)
        return res.replace("\"", "")

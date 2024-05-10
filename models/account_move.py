# -*- coding: utf-8 -*-
# Copyright (C) 2024 - S-DEV (<https://www.s-dev.com>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from dateutil.relativedelta import relativedelta

from odoo import fields, models, api, Command

class Account_Move(models.Model):
    _inherit = "account.move"
    invoice_note = fields.Html('Footer Note')
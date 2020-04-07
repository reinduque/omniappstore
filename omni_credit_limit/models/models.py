# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, float_compare
from odoo.exceptions import UserError
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import UserError, AccessError

class creditLimit(models.Model):
    _inherit = 'res.partner'

    allow_credit = fields.Boolean('Check Credit', default=False)
    #credit_limit = fields.Float('Credit Limit', default="0.0")
    credit_limit_on_hold = fields.Boolean('Credit Limit on hold', default=False)

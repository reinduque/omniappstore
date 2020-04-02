# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, float_compare
from odoo.exceptions import UserError
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import UserError, AccessError


class taxesPH(models.Model):
	_inherit = 'account.tax'



	atc_type = fields.Selection([
		('IND', 'INDIVIDUAL'),
		('CORP', 'CORPORATION'),
	], help="Select if ATC is a INDIVIDUAL or CORPORATION.")
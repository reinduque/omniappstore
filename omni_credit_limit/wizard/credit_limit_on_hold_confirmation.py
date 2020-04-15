# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import UserError, AccessError


class CreditLimitOnHoldConfirmation(models.TransientModel):
    _name = 'creditlimit.hold_confirmation'
    _description = 'Credit Limit on Hold Confirmation'


    sale_id = fields.Many2one('sale.order', string="Sale")
    msg = fields.Text()
    

    def confirm_creditlimitonhold(self):
        sale_order = self.env['sale.order'].browse([self.sale_id.id])
        partner = sale_order.partner_id
        partner.credit_limit_on_hold = True
        sale_order.action_confirm()
        return False
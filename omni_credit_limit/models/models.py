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
    credit_limit = fields.Float('Credit Limit', default="0.0")
    credit_limit_on_hold = fields.Boolean('Credit Limit on hold', default=False)


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('credit_limit', 'Credit Limit'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=4, default='draft')

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            order.check_limit()

        return res

    def check_limit(self):    
        self.ensure_one()
        partner = self.partner_id
        moveline_obj = self.env['account.move.line']
        movelines = moveline_obj.search(
            [('partner_id', '=', partner.id),
             ('account_id.user_type_id.name', 'in', ['Receivable', 'Payable']),
             ('full_reconcile_id', '=', False)]
        )
        debit, credit, total_unpaid = 0.0, 0.0, 0.0
        for line in movelines:
            credit += line.debit
            debit += line.credit
        sales = self.env['sale.order'].search([
            ('partner_id', '=', self.partner_id.id), 
            ('invoice_status', 'not in', [('invoiced')]),
            ('state','in',[('sale')])
            #i need to include state=done here. but state=sale is escluded when i add done
            ])
        msg = 'start'
        for sale in sales:
            total_unpaid += sale.amount_total
            msg = msg + '\nname='+sale.name+'::invoice_status='+sale.invoice_status+'::state='+sale.state+'::amount='+str(sale.amount_total)
        raise UserError(msg + '\nend'
            '\ncredit='+str(credit)+
            '\ndebit='+str(debit)+
            '\ntotal_unpaid='+str(total_unpaid)+
            '\npartner.credit_limit='+str(partner.credit_limit)
        )
        if (credit - debit + total_unpaid) > partner.credit_limit:
            if not partner.over_credit:
                msg = 'Confirming Sale Order is not allowed. \nTotal Due Amount =' \
                      '%s!\nPlease check Partner Accounts or Credit Limit.' % (credit - debit + total_unpaid)
                raise UserError(_('Credit Over Limits !\n' + msg))
            partner.write({'credit_limit': credit - debit + self.amount_total})

        return self

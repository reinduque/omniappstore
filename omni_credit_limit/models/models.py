# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, float_compare
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

    def action_confirm2(self):
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
            ('invoice_status', 'not in', ['invoiced']),
            ('state','in',['sale','done'])
            ])
        #msg = 'start'
        for sale in sales:
            total_unpaid += sale.amount_total
        #msg = msg + '\nname='+sale.name+'::invoice_status='+sale.invoice_status+'::state='+sale.state+'::amount='+str(sale.amount_total)
        #raise UserError(msg + '\nend'
        #    '\ncredit='+str(credit)+
        #    '\ndebit='+str(debit)+
        #    '\ntotal_unpaid='+str(total_unpaid)+
        #    '\npartner.credit_limit='+str(partner.credit_limit)
        #)
        if (credit - debit + total_unpaid) > partner.credit_limit and partner.allow_credit:
            if not partner.credit_limit_on_hold:
                if self.env.user.has_group('sales_team.group_sale_manager'):
                    msg = 'Total Due Amount %s will be above %s\'s credit limit %s.\n' \
                        'To confirm more sales, please process payment from Customer or raise Credit Limit.' \
                        % (credit - debit + total_unpaid, partner.name, partner.credit_limit)
                    view = self.env.ref('omni_credit_limit.credit_limit_on_hold_wizard_form')
                    wiz = self.env['creditlimit.hold_confirmation'].create({'sale_id': self.id,'msg':msg})
                    return {
                        'name': _('Put Credit Limit on Hold?'),
                        'type': 'ir.actions.act_window',
                        'view_mode': 'form',
                        'res_model': 'creditlimit.hold_confirmation',
                        'views': [(view.id, 'form')],
                        'view_id': view.id,
                        'target': 'new',
                        'res_id': wiz.id,
                        'context': self.env.context,
                    }
                else:
                    msg = 'Total Due Amount %s will be above %s\'s credit limit %s.' \
                      '\nTo confirm more sales, please process payment from Customer or raise Credit Limit.' \
                      '\nSale Order will not be confirmed.' % (credit - debit + total_unpaid, partner.name, partner.credit_limit)
                    raise UserError(_('Credit Limit Reached \n' + msg))
            else:
                msg = 'Total Due Amount %s will be above %s\'s credit limit %s.' \
                      '\nPartner\'s credit limit is currently on hold.' \
                      '\nTo confirm more sales, please process payment from Customer or raise Credit Limit.'\
                      '\nSale Order will not be confirmed.' % (credit - debit + total_unpaid, partner.name, partner.credit_limit)
                raise UserError(_('Credit Limit Reached \n' + msg))
        else:
            partner.write({'credit_limit_on_hold': False})
            self.action_confirm()
        return
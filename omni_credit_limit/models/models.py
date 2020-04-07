# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class omni_credit_limit(models.Model):
#     _name = 'omni_credit_limit.omni_credit_limit'
#     _description = 'omni_credit_limit.omni_credit_limit'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

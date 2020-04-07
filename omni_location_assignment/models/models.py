# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class omni_location_assignment(models.Model):
#     _name = 'omni_location_assignment.omni_location_assignment'
#     _description = 'omni_location_assignment.omni_location_assignment'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

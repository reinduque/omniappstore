# -*- coding: utf-8 -*-
# from odoo import http


# class OmniCreditLimit(http.Controller):
#     @http.route('/omni_credit_limit/omni_credit_limit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/omni_credit_limit/omni_credit_limit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('omni_credit_limit.listing', {
#             'root': '/omni_credit_limit/omni_credit_limit',
#             'objects': http.request.env['omni_credit_limit.omni_credit_limit'].search([]),
#         })

#     @http.route('/omni_credit_limit/omni_credit_limit/objects/<model("omni_credit_limit.omni_credit_limit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('omni_credit_limit.object', {
#             'object': obj
#         })

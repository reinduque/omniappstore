# -*- coding: utf-8 -*-
# from odoo import http


# class OmniLocationAssignment(http.Controller):
#     @http.route('/omni_location_assignment/omni_location_assignment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/omni_location_assignment/omni_location_assignment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('omni_location_assignment.listing', {
#             'root': '/omni_location_assignment/omni_location_assignment',
#             'objects': http.request.env['omni_location_assignment.omni_location_assignment'].search([]),
#         })

#     @http.route('/omni_location_assignment/omni_location_assignment/objects/<model("omni_location_assignment.omni_location_assignment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('omni_location_assignment.object', {
#             'object': obj
#         })

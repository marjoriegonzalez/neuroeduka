# -*- coding: utf-8 -*-
from odoo import http

# class Neuroeduka(http.Controller):
#     @http.route('/neuroeduka/neuroeduka/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/neuroeduka/neuroeduka/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('neuroeduka.listing', {
#             'root': '/neuroeduka/neuroeduka',
#             'objects': http.request.env['neuroeduka.neuroeduka'].search([]),
#         })

#     @http.route('/neuroeduka/neuroeduka/objects/<model("neuroeduka.neuroeduka"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('neuroeduka.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-
# from odoo import http


# class Projectreports(http.Controller):
#     @http.route('/projectreports/projectreports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/projectreports/projectreports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('projectreports.listing', {
#             'root': '/projectreports/projectreports',
#             'objects': http.request.env['projectreports.projectreports'].search([]),
#         })

#     @http.route('/projectreports/projectreports/objects/<model("projectreports.projectreports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('projectreports.object', {
#             'object': obj
#         })

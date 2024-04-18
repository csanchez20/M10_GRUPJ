# -*- coding: utf-8 -*-
# from odoo import http


# class Projectes(http.Controller):
#     @http.route('/projectes/projectes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/projectes/projectes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('projectes.listing', {
#             'root': '/projectes/projectes',
#             'objects': http.request.env['projectes.projectes'].search([]),
#         })

#     @http.route('/projectes/projectes/objects/<model("projectes.projectes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('projectes.object', {
#             'object': obj
#         })

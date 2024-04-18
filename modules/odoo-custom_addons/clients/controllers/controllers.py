# -*- coding: utf-8 -*-
# from odoo import http


# class Clients(http.Controller):
#     @http.route('/clients/clients', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clients/clients/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('clients.listing', {
#             'root': '/clients/clients',
#             'objects': http.request.env['clients.clients'].search([]),
#         })

#     @http.route('/clients/clients/objects/<model("clients.clients"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clients.object', {
#             'object': obj
#         })

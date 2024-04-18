# -*- coding: utf-8 -*-
# from odoo import http


# class GestioDeCalendari(http.Controller):
#     @http.route('/gestio_de_calendari/gestio_de_calendari', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestio_de_calendari/gestio_de_calendari/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestio_de_calendari.listing', {
#             'root': '/gestio_de_calendari/gestio_de_calendari',
#             'objects': http.request.env['gestio_de_calendari.gestio_de_calendari'].search([]),
#         })

#     @http.route('/gestio_de_calendari/gestio_de_calendari/objects/<model("gestio_de_calendari.gestio_de_calendari"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestio_de_calendari.object', {
#             'object': obj
#         })

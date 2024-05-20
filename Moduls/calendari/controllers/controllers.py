# -*- coding: utf-8 -*-
from odoo import http


class Calendari(http.Controller):
    @http.route('/calendari/calendari', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/calendari/calendari/objects', auth='public')
    def list(self, **kw):
        return http.request.render('calendari.listing', {
            'root': '/calendari/calendari',
            'objects': http.request.env['calendari.calendari'].search([]),
        })

    @http.route('/calendari/calendari/objects/<model("calendari.calendari"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('calendari.object', {
            'object': obj
        })

# -*- coding: utf-8 -*-
from odoo import http


class RecursosHumans(http.Controller):
    @http.route('/recursos_humans/recursos_humans', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/recursos_humans/recursos_humans/objects', auth='public')
    def list(self, **kw):
        return http.request.render('recursos_humans.listing', {
            'root': '/recursos_humans/recursos_humans',
            'objects': http.request.env['recursos_humans.recursos_humans'].search([]),
        })

    @http.route('/recursos_humans/recursos_humans/objects/<model("recursos_humans.recursos_humans"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('recursos_humans.object', {
            'object': obj
        })
    
    @http.route('/recursos_humanos/administra_personal', auth='public', methods=['GET'])
    def administra_personal(self, **kw):
        Empleado = http.request.env['recursos_humanos.empleado']
        data = Empleado.AdministraPersonal()
        return http.request.render('recursos_humanos.template_administra_personal', {
            'data': data
        })

    @http.route('/recursos_humanos/proceso_reclutamiento', auth='public', methods=['POST'], csrf=False)
    def proceso_reclutamiento(self, **kw):
        Empleado = http.request.env['recursos_humanos.empleado']
        nuevo_empleado = Empleado.ProcesoReclutamiento(
            nombre=kw.get('nombre'),
            apellidos=kw.get('apellidos'),
            cargo=kw.get('cargo'),
            salario=float(kw.get('salario'))
        )
        return http.request.render('recursos_humanos.template_proceso_reclutamiento', {
            'nuevo_empleado': nuevo_empleado
        })

    @http.route('/recursos_humanos/tiempo_libre', auth='public', methods=['POST'], csrf=False)
    def tiempo_libre(self, **kw):
        Empleado = http.request.env['recursos_humanos.empleado'].browse(int(kw.get('id_empleado')))
        Empleado.TiempoLibre(float(kw.get('horas')))
        return http.request.render('recursos_humanos.template_tiempo_libre', {
            'empleado': Empleado
        })

    @http.route('/recursos_humanos/evaluacion_desempeno', auth='public', methods=['POST'], csrf=False)
    def evaluacion_desempeno(self, **kw):
        Empleado = http.request.env['recursos_humanos.empleado'].browse(int(kw.get('id_empleado')))
        Empleado.EvaluacionDesempeño(kw.get('evaluacion'))
        return http.request.render('recursos_humanos.template_evaluacion_desempeno', {
            'empleado': Empleado
        })

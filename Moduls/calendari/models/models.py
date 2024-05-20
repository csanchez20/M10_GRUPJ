# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Calendari(models.Model):
    _name = 'calendari.calendari'
    _description = 'Calendari'

    name = fields.Char(string="Nom", required=True)
    value = fields.Integer(string="Valor")
    value2 = fields.Float(string="Valor Percentatge", compute="_compute_value_pc", store=True)
    description = fields.Text(string="Descripció")

    @api.depends('value')
    def _compute_value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100 if record.value else 0.0

    def afegir_cita(self, cita):
        if 'id_cita' in cita and 'fecha' in cita:
            self.env['calendari.cita'].create(cita)
        else:
            raise ValueError("Falten camps obligatoris per a crear una cita")

    def afegir_reunio(self, reunion):
        if 'id_reunion' in reunion and 'fecha' in reunion:
            self.env['calendari.reunion'].create(reunion)
        else:
            raise ValueError("Falten camps obligatoris per a crear una reunió")

    def afegir_visita(self, visita):
        if 'id_visita' in visita and 'fecha' in visita:
            self.env['calendari.visita'].create(visita)
        else:
            raise ValueError("Falten camps obligatoris per a crear una visita")


class Cita(models.Model):
    _name = 'calendari.cita'
    _description = 'Cita'

    id_cita = fields.Integer(string="ID Cita", required=True)
    fecha = fields.Date(string="Fecha", required=True)
    hora = fields.Float(string="Hora")
    ubicacion = fields.Char(string="Ubicación", size=255)
    descripcion = fields.Text(string="Descripción")
    cliente = fields.Char(string="Cliente")


class Reunion(models.Model):
    _name = 'calendari.reunion'
    _description = 'Reunión'

    id_reunion = fields.Integer(string="ID Reunión", required=True)
    fecha = fields.Date(string="Fecha", required=True)
    hora = fields.Float(string="Hora")
    ubicacion = fields.Char(string="Ubicación", size=255)
    descripcion = fields.Text(string="Descripción")
    asistentes = fields.Char(string="Asistentes", size=255)


class Visita(models.Model):
    _name = 'calendari.visita'
    _description = 'Visita'

    id_visita = fields.Integer(string="ID Visita", required=True)
    fecha = fields.Date(string="Fecha", required=True)
    hora = fields.Float(string="Hora")
    ubicacion = fields.Char(string="Ubicación", size=255)
    propiedad = fields.Char(string="Propiedad")
    descripcion = fields.Text(string="Descripción")
    cliente = fields.Char(string="Cliente")

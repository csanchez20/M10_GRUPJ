from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'casa_inteligente.cliente'
    _description = 'Clientes de Casa Inteligente'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo Electrónico')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Text(string='Dirección')
    prospecto = fields.Boolean(string='Es Prospecto')

class Prospecto(models.Model):
    _name = 'casa_inteligente.prospecto'
    _description = 'Prospectos de Casa Inteligente'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo Electrónico')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Text(string='Dirección')

class CasaInteligente(models.Model):
    _name = 'casa_inteligente.casa'
    _description = 'Casas Inteligentes'

    name = fields.Char(string='Nombre', required=True)
    ubicacion = fields.Char(string='Ubicación')
    maxima_velocidad_wifi = fields.Float(string='Máxima Velocidad WiFi')
    automatizaciones = fields.Text(string='Automatizaciones')

class ModuloGestionClientes(models.Model):
    _name = 'casa_inteligente.gestion_clientes'
    _description = 'Módulo de Gestión de Clientes'

    cliente_ids = fields.One2many('casa_inteligente.cliente', 'gestion_id', string='Clientes')
    prospecto_ids = fields.One2many('casa_inteligente.prospecto', 'gestion_id', string='Prospectos')

    @api.model
    def create_prospecto(self, vals):
        prospecto = self.env['casa_inteligente.prospecto'].create(vals)
        return {
            'name': 'Prospecto creado',
            'view_mode': 'form',
            'res_model': 'casa_inteligente.prospecto',
            'res_id': prospecto.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

    @api.model
    def create_cliente(self, vals):
        cliente = self.env['casa_inteligente.cliente'].create(vals)
        return {
            'name': 'Cliente creado',
            'view_mode': 'form',
            'res_model': 'casa_inteligente.cliente',
            'res_id': cliente.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

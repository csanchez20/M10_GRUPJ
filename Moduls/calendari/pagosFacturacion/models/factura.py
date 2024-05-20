# models/factura.py

from odoo import models, fields

class Factura(models.Model):
    _name = 'gestion.factura'
    _description = 'Factura'

    name = fields.Char(string='Número de Factura', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    total = fields.Float(string='Total', required=True)
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('pagado', 'Pagado'),
        ('cancelado', 'Cancelado')
    ], string='Estado', default='borrador')


# models/pago.py

from odoo import models, fields

class Pago(models.Model):
    _name = 'gestion.pago'
    _description = 'Pago'

    name = fields.Char(string='Referencia del Pago', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    factura_id = fields.Many2one('gestion.factura', string='Factura', required=True)
    monto = fields.Float(string='Monto', required=True)
    metodo_pago = fields.Selection([
        ('transferencia', 'Transferencia Bancaria'),
        ('tarjeta', 'Tarjeta de Crédito/Débito'),
        ('efectivo', 'Efectivo')
    ], string='Método de Pago', required=True)

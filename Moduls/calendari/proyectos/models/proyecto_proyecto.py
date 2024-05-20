# models/proyecto_proyecto.py

from odoo import models, fields

class ProyectoProyecto(models.Model):
    _inherit = 'project.project'

    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    direccion = fields.Char(string='Dirección', required=True)
    precio = fields.Float(string='Precio del Proyecto', required=True)
    fecha_inicio = fields.Date(string='Fecha de Inicio')
    fecha_fin = fields.Date(string='Fecha de Finalización')
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('en_progreso', 'En Progreso'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado')
    ], string='Estado', default='borrador')

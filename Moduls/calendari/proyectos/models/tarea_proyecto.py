# models/tarea_proyecto.py

from odoo import models, fields

class TareaProyecto(models.Model):
    _inherit = 'project.task'

    nombre_vivienda = fields.Char(string='Nombre de la Vivienda')
    estado_digitalizacion = fields.Selection([
        ('no_iniciado', 'No Iniciado'),
        ('en_progreso', 'En Progreso'),
        ('completado', 'Completado')
    ], string='Estado de Digitalización', default='no_iniciado')
    tipo_tarea = fields.Selection([
        ('renovacion', 'Renovación'),
        ('automatizacion', 'Automatización')
    ], string='Tipo de Tarea', default='renovacion')

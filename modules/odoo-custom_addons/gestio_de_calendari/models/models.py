# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gestio_de_calendari(models.Model):
#     _name = 'gestio_de_calendari.gestio_de_calendari'
#     _description = 'gestio_de_calendari.gestio_de_calendari'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

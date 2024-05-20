# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Empleado(models.Model):
    _name = 'recursos_humanos.empleado'
    _description = 'Empleado'

    id_empleado = fields.Integer(string="ID Empleado")
    nombre = fields.Char(string="Nombre")
    apellidos = fields.Char(string="Apellidos")
    cargo = fields.Char(string="Cargo")
    fecha_contrato = fields.Date(string="Fecha de Contrato")
    salario = fields.Float(string="Salario")
    tiempo_libre = fields.Float(string="Tiempo Libre")
    evaluacion_desempeño = fields.Char(string="Evaluación de Desempeño")

    def AdministraPersonal(self):
        empleados = self.search([])
        total_empleados = len(empleados)
        empleados_info = [(emp.id_empleado, emp.nombre, emp.apellidos) for emp in empleados]
        print(f"Total de Empleados: {total_empleados}")
        print(f"Empleados Info: {empleados_info}")
        return {'total_empleados': total_empleados, 'empleados': empleados_info}

    def ProcesoReclutamiento(self):
        nuevo_empleado = self.create({
            'id_empleado': 2,
            'nombre': 'Maria',
            'apellidos': 'Perez',
            'cargo': 'Analista',
            'fecha_contrato': '2023-05-01',
            'salario': 1500.0,
            'tiempo_libre': 30.0,
            'evaluacion_desempeño': 'B'
        })
        print(f"Nuevo Empleado: {nuevo_empleado}")
        return nuevo_empleado

    def TiempoLibre(self):
        self.tiempo_libre += 1  
        print(f"Tiempo Libre Actualizado: {self.tiempo_libre} hores per a {self.nombre} {self.apellidos}")
        return self.tiempo_libre

    def EvaluacionDesempeño(self):
        self.evaluacion_desempeño = 'A+'
        print(f"Evaluación de Desempeño Actualizada: {self.evaluacion_desempeño} per a {self.nombre} {self.apellidos}")
        return self.evaluacion_desempeño
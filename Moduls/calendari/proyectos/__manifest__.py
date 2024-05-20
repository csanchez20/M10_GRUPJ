# __manifest__.py

{
    'name': 'Gestión de Proyectos Inmobiliarios',
    'version': '1.0',
    'summary': 'Gestión de proyectos de renovación y automatización del hogar',
    'description': 'Módulo para gestionar proyectos de renovación y automatización de viviendas, incluyendo la asignación de tareas, plazos y seguimiento del progreso.',
    'author': 'Tu Nombre',
    'depends': ['base', 'project', 'contacts', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/tarea_proyecto_vistas.xml',
        'views/proyecto_proyecto_vistas.xml',
    ],
    'installable': True,
    'application': True,
}

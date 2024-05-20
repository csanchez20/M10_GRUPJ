# __manifest__.py

{
    'name': 'Gestión de Pagos y Facturación',
    'version': '1.0',
    'summary': 'Control de los gastos de la empresa',
    'description': 'Módulo para gestionar pagos y facturas, permitiendo un control detallado de los gastos de la empresa.',
    'author': 'Tu Nombre',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/factura_views.xml',
        'views/pago_views.xml',
    ],
    'installable': True,
    'application': True,
}

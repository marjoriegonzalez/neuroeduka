# -*- coding: utf-8 -*-
{
    'name': "neuroeduka",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Sistema de Gestión para Centro Médico y Terapeutico NeuroEduka
    """,

    'author': "Javiera Bazaes, Marjorie González, Jorge Meza",
    'website': "http://www.neuroeduka.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menus.xml',
        'views/especialidad.xml',
        'views/especialista.xml',
        'views/box.xml',
        'views/paciente.xml',
        'views/terapia.xml',
        'views/parentesco.xml',
        'views/familiar.xml',
        'views/tratamiento.xml',
        'views/reserva.xml',
        'views/motivo_consulta.xml',
        'views/diagnostico.xml',
        'views/consulta.xml',
        'views/administrador.xml',
        'views/proveedor.xml',
        'views/producto.xml',
        'views/detalle_factura.xml',
        'views/factura.xml',
        'views/periodo.xml',
        'views/resultado_operacional.xml',
        'views/boleta_pago.xml',
        'views/evolucion.xml',
        'views/recurso.xml',
        'views/dato_anamnesico.xml',
        'views/centro_educativo.xml',
    
        

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
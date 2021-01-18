# -*- coding: utf-8 -*-
{
    'name': "Project Reports",

    'summary': """Reportes de los proyectos""",

    'description': """
        Project Reports es un modulo para hacer reportes de los proyectos
            - Reporte de las tareas, las actividades y los partes de hora
    """,

    'author': "Marta Garcia",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
        'views/projectreports.xml', 
        # 'views/projectreports_project.xml'
        'report/reporte.xml', 

    ],
    'images': [
        'static/src/img/logo.png',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

# -*- coding: utf-8 -*-
{
    'name': "Process Control - Enviar tareas por mail",

    'summary': """""",

    'description': """
            Enviar tareas por mail
    """,

    'author': "Process Control",
    'website': "http://www.processcontrol.es",
    'category': 'Revenues',
    'version': '14.0.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'project',
    ],

    # always loaded
    'data': [
        'report/report_services_part.xml',
        'data/mail_data.xml',
        'data/task_data.xml',
        'views/project_view.xml',
        'views/task_view.xml',
        'views/templates.xml',
    ]
    # only loaded in demonstration mode
    # 'demo': [
    # 'demo/demo.xml',
    # ],
}

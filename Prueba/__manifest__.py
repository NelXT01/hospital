# -*- coding: utf-8 -*-
{
    'name': 'Prueba con indio Hospital',
    'version': '1',
    'summary': 'Ejercicios',
    'sequence': -100,
    'description': """Solo prueba""",
    'author': 'Yo Nelson',
    'maintainer': 'Yo',
    'website': 'https://www.odoomates.tech',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'mail',
            ],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/sale.xml',
        'data/data.xml',
        'data/mail_template.xml',
        'views/kids_view.xml',
        'views/male_patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'report/patient_card.xml',
        'report/report.xml',



            ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/hospital.jpg'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
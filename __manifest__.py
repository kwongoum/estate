# -*- coding: utf-8 -*-
{
    'name': 'Estate',
    'version': '1.0',
    'category': 'App',
    'summary': 'Manage properties and estates',
    'description': 'Module for managing estates, properties, and customer relations.',
    'author': 'Avit Wongoum',
    'depends': ['base','mail'],
    'application': True,
     'data': [
        'security/ir.model.access.csv',
        'data/res_partner_data.xml',
        'views/estate_property.xml',
        'views/estate_property_actions.xml',
        'views/menu.xml',
        'data/estate.property.csv',
        'views/schedulers/estate_property_scheduler.xml',
      #   'data/templates/example_email_template.xml'
       
     ]

}

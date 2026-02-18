# -*- coding: utf-8 -*-
{
  'name': 'Estate',
  'version': '19.0.1.0.0',
  'summary': 'Modulo para la Gestión Inmobiliaria',
  'description': """
  """,
  'author': 'Alberto A. Mártir González',
  'license': 'LGPL-3',
  'depends': [
    'base',
  ],
  'data': [
    # security
    'security/ir.model.access.csv',
    
    # views
    'views/estate_property_views.xml',
    
    # menus
    'views/estate_menus.xml',
  ],
  'installable': True,
  'application': True,
  'auto_install': False
}
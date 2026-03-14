from odoo import fields,models

class EstatePropertyType(models.Model):
  """Modelo para deifinir tipos de propiedades"""
  _name = 'estate.property.type'
  _description = 'Property Type'
  
  name = fields.Char(
    string='Property Type',
    help='Indicate the type of property',
    required=True
  )
from odoo import fields,models

class EstateProperty(models.Model):
  _name = 'estate.property'
  _description = 'Estate Property'
  
  name = fields.Char(
    string='Property Name',
    required=True
  )
  
  description = fields.Text(
    string='Description'
  )
  
  postcode = fields.Char(
    string='Postal Code'
  )
  
  date_availability = fields.Date(
    string='Date Availability',
    copy=False
  )
  
  expected_price = fields.Float(
    string='Expected Price',
    required=True
  )
  
  selling_price = fields.Float(
    string='Selling Price',
    readonly=True,
    copy=False
  )
  
  bedrooms = fields.Integer(
    string='Bedrooms'
  )
  
  living_area = fields.Integer(
    string='Living Area'
  )
  
  facades = fields.Integer(
    string='Facades'
  )
  
  garage = fields.Boolean(
    string='Garage',
    default=False,
    help='Indicate if it has a garage'
  )
  
  garden = fields.Boolean(
    string='Garden',
    default=False,
    help='Indicate if it has a garden'
  )
  
  garden_area = fields.Integer(
    string='Garden Area'
  )
  
  garden_orientation = fields.Selection(
    string='Garden Orientation',
    selection=[
      ('north','North'),
      ('south','South'),
      ('east','East'),
      ('west','West')
    ],
    help='Indicate the orientation of the garden'
  )
from odoo import fields,models
from datetime import timedelta

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
    copy=False,
    default=lambda self: fields.Date.today() + timedelta(days=90)
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
    string='Bedrooms',
    default=2
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
  
  active = fields.Boolean(
    string='Active',
    default=True
  )
  
  state = fields.Selection(
    string='State',
    selection=[
      ('new','New'),
      ('offer received','Offer Received'),
      ('offer accepted','Offer Accepted'),
      ('sold','Sold'),
      ('cancelled','Cancelled')
    ],
    help='Indicate the state of the property',
    default='new'
  )
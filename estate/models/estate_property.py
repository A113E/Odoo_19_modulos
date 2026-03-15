from odoo import fields,models
from datetime import timedelta

class EstateProperty(models.Model):
  """Modelo para definir propiedades"""
  _name = 'estate.property'
  _description = 'Estate Property'
  
  name = fields.Char(
    string='Property Name',
    required=True
  )
  # Campos relacionales
  property_type_id = fields.Many2one(
    'estate.property.type',
    string='Property Type',
    required=True
  )
  
  user_id = fields.Many2one(
    'res.users',
    string='Salesperson',
    index=True, # para busqueda rapida
    tracking=True, # para registrar cambios en el chatter (True toma como valor 100 en importancia)
    default=lambda self: self.env.user # Toma el registro del usuario actual por defecto
  )
  
  partner_id = fields.Many2one(
    'res.partner',
    string='Buyer',
    index=True,
    tracking=10, #  el numero 10 hace que este sea el chatter con mas prioridad en la lista 
    domain="['|', ('company_id','=', False), ('company_id','=', 'company_id')]", # Filtra por compradores que no tengan compañias o que pertenezcan a la compañia del documento
    copy=False
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
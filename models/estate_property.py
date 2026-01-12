from odoo import models, fields
class EstateProperty(models.Model):
	_name = "estate.property"
	_description = "Estate Property"
	name = fields.Char(required=True)
	description = fields.Text(default=" good deal !")
	postcode = fields.Char()
	date_availability = fields.Date(default=fields.Datetime.now)
	expected_price = fields.Float(default=1000000.0)
	selling_price = fields.Float()
	bedrooms = fields.Integer()
	living_area = fields.Integer()
	facades = fields.Integer()
	garage = fields.Boolean()
	garden= fields.Boolean()
	garden_area = fields.Integer()
	last_seen = fields.Datetime(default=fields.Datetime.now)
	garden_orientation = fields.Selection(
	    selection=[ ("N", "North"), ("S", "South"), ("E", "East"),  ("W", "West"),],
	    string="Garden Orientation",
	)
from odoo import models, fields
from odoo.exceptions import ValidationError, UserError
class EstatePropertyType(models.Model):
	_name = "estate.property.type"
	_description = " Property Type"
	_order="sequence,name"
	
	name = fields.Char("Name", required=True)
	sequence = fields.Integer("sequence", default=10)
	description = fields.Text(default=" type of property !")

	_sql_constraints = [
		("ckeck_name", "UNIQUE(name)", "The name must be unique !")
	]
	
	property_ids=fields.One2many("estate.property", "property_type_id", string="Properties")

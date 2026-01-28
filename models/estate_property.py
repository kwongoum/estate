from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
class EstateProperty(models.Model):
	_name = "estate.property"
	_description = "Estate Property"
	_order="date_availability desc"
	name = fields.Char(required=True)
	description = fields.Text(default=" good deal !")
	postcode = fields.Char()
	date_availability = fields.Date(default=fields.Datetime.now)
	expected_price = fields.Float(default=110.0)
	selling_price = fields.Float()
	bedrooms = fields.Integer()
	living_area = fields.Integer(default=0)
	facades = fields.Integer()
	garage = fields.Boolean()
	garden= fields.Boolean()
	garden_area = fields.Integer(default=0)
	last_seen = fields.Datetime(default=fields.Datetime.now)
	garden_orientation = fields.Selection(
	    selection=[ ("N", "North"), ("S", "South"), ("E", "East"),  ("W", "West"),],
	    string="Garden Orientation",
	)
	user_id = fields.Many2one("res.users",string="saleman", default=lambda self: self.env.user)
	buyer_id = fields.Many2one("res.partner", string="Buyer", readonly="True",copy="False", 
							default=lambda self: self.env.ref('estate.default_buyer_test').id )
	
	property_type_id = fields.Many2one("estate.property.type", string="Property Type")
	property_offer_ids= fields.One2many("estate.property.offer", "estate_property_id", string="Offers")
	property_tag_ids  =  fields.Many2many("estate.property.tag", string="Tags")
	state=fields.Selection(
		selection=[("new","New"),("ready","Ready"),("offer_received","Offer received"),("offer_accepted","Offer accepted"),
			 		("sold","Sold"),("canceled","Canceled")],
		string="Status",
		required="True",
		copy="False",
		default="new"
	)

	def action_sold(self):
		if "canceled" in self.mapped("state"):
			raise UserError("cancelled properties cannot be sold")
		return self.write({"state":"sold"})
	
	def action_cancel(self):
		if "sold" in self.mapped("state"):
			raise UserError("sold properties cannot be cancelled")
		return self.write({"state":"canceled"})

	total_area=fields.Integer(readonly=True, 
						   compute ='_compute_total_area',
						   store=True
						   )
    @api.depends("living_area","garden_area")	
	def _compute_total_area(self):
		for prop in self: 
			prop.total_area=(prop.living_area or 0)+(prop.garden_area or 0)

	_sql_constraints = [
		(
			'check_expected_price_positive',
			'CHECK(expected_price > 0)',
			'a property expected price MUST BE strictly positive'

		),
		(
			'check_property_name_is_unique',
			'UNIQUE(name)',
			'Property name MUST be unique'
		),
		(
			'check_selling_price_non_negative',
			'CHECK(selling_price >= 0.0)',
			'Selling price cannot be negative'
		)
	]

	@api.constrains('selling_price','expected_price')
	def _check_selling_price_standard(self):
		for record in self:
			if record.selling_price!=0.00 and record.selling_price < record.expected_price:
				raise ValidationError("Selling price cannot be inferior to expected price")
			

	

	""" @api.onchange("garden")
	def _onchange_garden(self):
		if self.garden:
			self.garden_area=self.garden_area
			self.garden_orientation="N"
		else:
			self.garden_area=0
			self.garden_orientation=False """

	@api.model
	def create(self,vals):

		if vals.get("selling_price") and vals.get("date_availability"):
			vals["state"]="ready"
		return super().create(vals)
	
	def unlink(self):

		if not set(self.mapped("state")) <={"new", "canceled"}:
			raise UserError("only new and canceled state can be deleted.")
		return super().unlink()
	
	def update_state_schedule(self):
		properties = self.env["estate.property"].search([
			('date_availability', '=', False),
        	('state', '!=', 'canceled')
			])
		properties.write({'state': 'canceled'})

	def action_send_email(self):
		template=self.env.ref("estate.simple_example_email_template") 
		
		email_values={
			"email_to":"avit.14@hotmail.com,avit.wongoum@gmail.com",
			"email_cc":False,
			"auto_delete":True,
			"recipient_ids": [],
            "partner_ids": [],
            "scheduled_date": False,
            "email_from": "avit.wongoum@gmail.com",
		}
		template.send_email(
			self.id,
			email_values=email_values,
			force_send=True

		)

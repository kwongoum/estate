from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tags"
    
    _sql_constraints = [
        ("check_price", "CHECK(price > 0)", "The price must be strictly positive"),
    ]

    name = fields.Char("Name", required=True)
    color = fields.Integer(default=4)

    # estate_property_ids =  fields.Many2many("estate.property")
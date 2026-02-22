from odoo import fields, models, api
from odoo.exceptions import ValidationError


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"

    _sql_constraints = [
        ("check_price", "CHECK(price > 0)", "The price must be strictly positive"),
    ]

    name = fields.Char("Name", required=True)
    color = fields.Integer(default=4)

    # estate_property_ids =  fields.Many2many("estate.property")
    @api.constrains("color")
    def _check_color(self):
        for record in self:
            if record.color > 100000:
                raise ValidationError("Color Index must be less than 100000")

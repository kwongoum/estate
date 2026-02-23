# -*- coding: utf-8 -*-
{
    "name": "Estate",
    "version": "17.0.1.0.0",
    "category": "App",
    "summary": "Manage properties and estates",
    "description": "Module for managing estates, properties, and customer relations.",
    "author": "Avit Wongoum",
    "depends": ["base", "mail"],
    "application": True,
    "data": [
        "security/ir.model.access.csv",
        "data/res_partner_data.xml",
        "views/estate_property.xml",
        "views/estate_property_offer.xml",
        "views/estate_property_type.xml",
        "views/estate_property_tag.xml",
        "views/estate_property_actions.xml",
        "views/estate_property_type_actions.xml",
        "views/estate_property_offer_actions.xml",
        "views/estate_property_tag_actions.xml",
        "views/menu.xml",
        "views/reports/output_pdf/estate_property_report.xml",
        "data/estate.property.csv",
        "views/schedulers/estate_property_scheduler.xml",
        "views/users.xml",
        #  'data/templates/example_email_template.xml'
        #  'data/res.groups.csv',
        #  'data/ir.model.access.csv'
        # demo data
        "demo/estate_property_tag.xml",
    ],
}

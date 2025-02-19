from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_owner = fields.Boolean('Is Owner')
    property_ids = fields.One2many(
        'estate.property',
        'partner_id',
        string='Properties'
    )

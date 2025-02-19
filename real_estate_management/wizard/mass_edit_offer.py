from odoo import models, fields, api

class MassEditOffer(models.TransientModel):
    _name = 'mass.edit.offer'
    _description = 'Mass Edit Offer'

    property_ids = fields.Many2many('estate.property', string='Properties')
    new_price = fields.Float(string='New Price')
    buyer_id = fields.Many2one('res.partner', string='Buyer')

    def default_get(self, fields):
        res = super(MassEditOffer, self).default_get(fields)
        
        active_ids = self.env.context.get('active_ids')
        if active_ids:
            res['property_ids'] = [(6, 0, active_ids)]
        return res

    def create_offer(self):
        for property in self.property_ids:
            self.env['estate.property.offer'].create({
                'estate_property_id': property.id,
                'buyer_id': self.buyer_id.id,
                'price': self.new_price,
                'date_of_offer': fields.Date.today(),
            })
from odoo import models, fields, api
from odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'
    _sql_constraints = [
       ('offer_unique', 'UNIQUE(estate_property_id,buyer_id,price)', 'The offer must be unique by amount and property.')
   ]

    estate_property_id = fields.Many2one(
        'estate.property',
        string='Property',
        required=True,
    )
    agent_id = fields.Many2one(related='estate_property_id.user_id', string='Agent Commercial')
    buyer_id = fields.Many2one(
        'res.partner',
        string='Buyer',
        required=True,
    )
    seller_id = fields.Many2one(
        'res.partner',
        related='estate_property_id.partner_id',
        string='Seller',
        required=True,
    )
    date_of_offer = fields.Date(
        string='Date Of Offer',
        required=True,
    )
    price = fields.Float(
        string='Price',
        required=True,
    )

    def accept_offer(self):
        self.ensure_one()
        category = self.env.ref('real_estate_management.estate_property_category_win')
        self.estate_property_id.property_category_id = category.id
        return {
                'effect': {
                    'fadeout': 'slow',
                    'message': "SUPER %s" % self.env.user.name,
                    'img_url': '/web/image/%s/%s/image_1024' % (self.env.user._name, self.env.user.id) if self.env.user.image_1024 else '/web/static/img/smile.svg',
                    'type': 'rainbow_man',
                }
            }
    
    def decline_offer(self):
        self.ensure_one()
        category = self.env.ref('real_estate_management.estate_property_category_lose')
        self.estate_property_id.property_category_id = category
    
    # @api.constrains('price', 'estate_property_id')
    # def _check_price(self):
    #     for record in self:
    #         if self.price < self.estate_property_id.estimation_price:
    #             raise UserError("ERRREUR CONTRAINTE.")

    # @api.onchange('price', 'estate_property_id')
    # def _onchange_price(self):
    #     if self.price and self.estate_property_id:
    #         if self.price < self.estate_property_id.estimation_price:
    #             raise UserError("ERRREUR.")


    def _compute_display_name(self):
        for record in self:
            record.display_name = f'{record.buyer_id.name} - {record.price}'

    @api.model
    def create(self, vals):
        record = super(EstatePropertyOffer, self).create(vals)
        if record.estate_property_id:
            category = self.search_or_create()
            if category:
                record.estate_property_id.property_category_id = category.id
        return record

    def search_or_create(self):
        category = self.env['estate.property.category'].search([('name', '=', 'En vente !')])
        if not category:
            category = self.env['estate.property.category'].create({
                'name': 'En vente !',
                'description': 'Test',
            })
        return category
    


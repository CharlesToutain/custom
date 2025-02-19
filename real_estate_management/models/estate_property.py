from datetime import timedelta
from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = 'estate.property'
    _inherit = ['mail.thread.main.attachment', 'mail.activity.mixin']
    _description = 'Estate Property'
    _sql_constraints = [
        ('check_surface', 'CHECK(surface > 0)', 'The surface of a property must be positive.'),
        ('name_unique', 'UNIQUE(name)', 'The title of the property must be unique.')
    ]
    

    name = fields.Char(string='Title', required=True)
    description = fields.Html(
        string='Description',
        help='A detailed description of the property',
    )
    property_category_id = fields.Many2one(
        'estate.property.category',
        string='Category',
    )
    street = fields.Char('street')
    zip = fields.Char('zip')
    country_id = fields.Many2one('res.country', string='country')
    surface = fields.Float('surface')
    type = fields.Selection([
        ('studio', 'Studio'),
        ('t1', 'T1'),
        ('t2', 'T2'),
        ('t3', 'T3'),
        ('t4', 'T4'),
        ('t5', 'T5'),
    ], string='type')
    date_of_build = fields.Date('Date Of Build')
    picture = fields.Binary('Picture')
    tag_ids = fields.Many2many('estate.property.tag', string='tag')
    partner_id = fields.Many2one('res.partner', string='Owner')
    partner_street = fields.Char(related='partner_id.street', string='Owner Street')
    partner_email = fields.Char(related='partner_id.email', string='Owner Email')
    is_appartment = fields.Boolean(
        'Is Appartment',
        compute='_compute_is_appartment',
    )
    date_of_last_dpe = fields.Date('Date Of Last DPE')
    is_valid_dpe = fields.Boolean(
        'Is Valid DPE',
        store=True,
        compute='_compute_is_valid_dpe',
    )
    is_for_rent = fields.Boolean(
        'Is For Rent',
    )
    estimation_price = fields.Float('Estimation Price')
    user_id = fields.Many2one('res.users', string='Responsible')

    @api.depends('date_of_last_dpe')
    def _compute_is_valid_dpe(self):
        for rec in self:
            if rec.date_of_last_dpe:
                days_difference = fields.Date.today() - rec.date_of_last_dpe
                rec.is_valid_dpe = days_difference <= timedelta(days=730)
            else:
                rec.is_valid_dpe = False

    def _compute_is_appartment(self):
        for rec in self:
            rec.is_appartment = rec.type in ['t1', 't2', 't3', 't4', 't5']

    def open_contact(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'res_id': self.partner_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
    # def open_wizard(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Mass Edit Offer',
    #         'res_model': 'mass.edit.offer',
    #         'view_mode': 'form',
    #         'target': 'new',
    #     }
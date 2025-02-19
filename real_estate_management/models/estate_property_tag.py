from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Tag'


    name = fields.Char('name')
    property_count = fields.Integer(
        string='Property Count',
        compute='_compute_property_count'
    )

    def _compute_property_count(self):
        for record in self:
            record.property_count = len(self.env['estate.property'].search([('tag_ids', 'in', record.id)]))
            

    def action_properties(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Properties',
            'res_model': 'estate.property',
            'view_mode': 'list,form',
            'domain': [('tag_ids', 'in', self.id)],
            'context': {'group_by': 'partner_id'},
        }
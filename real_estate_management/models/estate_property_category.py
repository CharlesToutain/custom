from odoo import models, fields

class EstatePropertyCategory(models.Model):
    _name = 'estate.property.category'
    _description = 'Estate Property Category'
    
    name = fields.Char('name')
    description = fields.Text('description')
    is_for_rent = fields.Boolean('is_for_rent')
    # le one2many permet de créer une relation one2many entre les deux modèles
    # property_category_id correspond à la relation inverse, c'est-à-dire le champ Many2one dans le modèle EstateProperty
    property_ids = fields.One2many(
        'estate.property', 
        'property_category_id', string='Properties')
    

    def write(self, vals):
        res = super(EstatePropertyCategory, self).write(vals)
        if 'is_for_rent' in vals:
            for record in self:
                record.property_ids.write({'is_for_rent': vals['is_for_rent']})
        return res
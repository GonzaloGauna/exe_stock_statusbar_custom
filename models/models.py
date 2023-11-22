# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError

class StockPickingCustomization(models.Model):
    _inherit = 'stock.picking'

    def action_success(self):
        self.state='succeced'

    def action_sent(self):
        self.state='sent'

    def custom_action_done(self):
        self.state='done'

    def action_return_success(self):
        self.state='sent'

    def button_validate(self):
        res= super(StockPickingCustomization,self).button_validate()


    state_a = fields.Selection(related='state')
    state_b = fields.Selection(related='state')
    warehouse_id = fields.Many2one(related='picking_type_id.warehouse_id')
    state = fields.Selection(selection_add=[('done',),('sent','Tránsito'),('succeced','Conforme')])
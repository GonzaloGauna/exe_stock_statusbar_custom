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
        # employee=self.env['hr.employee'].search([('work_email','=',self.user_email),('picking_password','=',self.password)])
        # if(len(employee)==1):
        # if(self.user_id and self.user_id.employee_count>0 and self.user_id.employee_ids[0].picking_password == self.password):
            res= super(StockPickingCustomization,self).button_validate()
            # self.user_validation=employee.work_email
        # else:
        #     raise UserError(_('La constraseña de inventario no es válida.'))
#        res= super(StockPickingCustomization,self).button_validate()
        # if(self.warehouse_id.id == 1):
        #    self.user_id=self.env.user
        # return res

    state_a = fields.Selection(related='state')
    state_b = fields.Selection(related='state')
    warehouse_id = fields.Many2one(related='picking_type_id.warehouse_id')
 #   code_operation = fields.Selection(related='warehouse_id.code')
    # user_email =  fields.Char("Correo de validación")
    # password = fields.Char("Clave de validación")
    # user_validation =  fields.Char("Validado por")
    state = fields.Selection(selection_add=[('done',),('sent','Tránsito'),('succeced','Conforme')])
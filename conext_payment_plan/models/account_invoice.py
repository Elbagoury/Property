from openerp import models, fields, api, _

class AccountInvoice(models.Model):
    _inherit = "account.invoice"


    order_id = fields.Many2one(comodel_name="property.sale", string="Order ID")
    payment_plan_ids  = fields.One2many('payment.plan','invoice_id','Payment Plans')
    
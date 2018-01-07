from odoo import models, fields, api, _
from datetime import date

class PaymentPlan(models.Model):
    _inherit = "payment.plan"

    
    @api.model
    def create(self,vals):
        vals['name'] = self.env['ir.sequence'].get('payment.plan') or '/'
        return super(PaymentPlan,self).create(vals)

    
    name = fields.Char("Name",default = "/")
#    date_due = fields.Date("Date",required = True,default = date.today().strftime('%Y-%m-%d'))
#    amount_total = fields.Float("Amount",required=True)
    journal_id = fields.Many2one("account.journal","Method Of Payment")
#    partner_id = fields.Many2one(comodel_name = 'res.partner',string = "Partner")
#    invoice_id = fields.Many2one('account.invoice',string = "Invoice", ondelete='cascade', index=True)
#    state = fields.Selection([('unpaid','Not Paid'),('paid','Paid')],string = 'State',default = "unpaid")
    sequence = fields.Integer(string= "Sequence")


from odoo import api,fields,models,_
from odoo.exceptions import UserError

confirm =[('draft','Draft'),('confirm','confirm'),('booking_fee_created','Booking Fee Created'),('cancel','cancel'),('sp','SP')]

class booking(models.Model):
    _name ="booking.fee"
    
    @api.model
    def _default_company_id(self):
        user = self.env['res.users'].browse(self.env.uid)
        return user.company_id.id

    name = fields.Char(string="No.Pemesanan", default="/")
    team_id = fields.Many2one('crm.team', string="Type")
    currency_id = fields.Many2one('res.currency', string="Currency")
    dp_account = fields.Many2one('account.account', string="Account")
    is_reserved = fields.Boolean(string="Sudah Reservasi")
    reserved_id = fields.Many2one(comodel_name="reserved", string="No. Reservasi")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Nama Kustomer")
    sale_order_id = fields.Many2one(comodel_name="sale.order", string="Sales Order")	
    booking_date = fields.Date(string="Tanggal Pemesanan")
    property_unit_id = fields.Many2one(comodel_name="product.template", string="Unit Properti")
    amount = fields.Float(string="Jumlah Harga Booking")
    notes = fields.Char(string="Catatan")
    state = fields.Selection(string="Status", selection=confirm, required=True,readonly=True,default=confirm[0][0])
    company_id = fields.Many2one(comodel_name="res.company", string="Nama Company/Divisi", default=_default_company_id)
    invoice_id = fields.Many2one(comodel_name="account.invoice",  string="ID Invoice")

    @api.multi
    def button_draft(self):
        self.state = confirm[0][0]
        
    @api.multi
    def button_confirmed(self):
        if self.name == '/':
            number = self.env['ir.sequence'].get('booking_property')
            self.name = number
        self.state = confirm[1][0]
 
    @api.multi
    @api.onchange('reserved_id')
    def onchange_reserved_id(self):
        values = {
            'partner_id': False,
            'sale_order_id': False,
            'property_unit_id': False,
        }
        if self.reserved_id :
            values['partner_id'] = self.reserved_id.partner_id.id
            values['property_unit_id'] = self.reserved_id.property_unit_id.id
            values['sale_order_id'] = self.reserved_id.sale_order_id.id
        self.update(values)
 
    # @api.multi
    # def button_create_booking_fee(self):
        # sale_orders = self.reserved_id.sale_order_id		
        # wizard_id = self.env['sale.advance.payment.inv'].create({'advance_payment_method':'all'})
        # res = wizard_id.with_context(open_invoices = True,active_ids = sale_orders.id).create_invoices()
        # account_invoice = self.env['account.invoice'].search([('id','=',res.get('res_id',False))],limit=1)
        # account_invoice.with_context(type = 'out_invoice', journal_type =  'sale').action_invoice_open()

        # if self._context.get('open_invoices', False):
            # self.state = 'booking_fee_created'
            # return sale_orders.action_view_invoice()

    @api.multi
    def button_create_booking_fee(self):
        inv_obj = self.env['account.invoice']
        ir_property_obj = self.env['ir.property']

        if self.amount <= 0.00:
            raise UserError(_('Booking fee cannot be made with amount less then 0'))
        for order in self :
            invoice = inv_obj.create({
                'name': order.name,
                'origin': order.name,
                'type': 'out_invoice',
                'reference': False,
                'account_id': order.partner_id.property_account_receivable_id.id,
                'partner_id': order.partner_id.id,
                #'partner_shipping_id': order.partner_shipping_id.id,
                'invoice_line_ids': [(0, 0, {
                    'name': order.name,
                    'origin': order.name,
                    'account_id': order.dp_account.id,
                    'price_unit': order.amount,
                    'quantity': 1.0,
                    'discount': 0.0,
                    # 'uom_id': self.property_unit_id.uom_id.id,
                    #'product_id': self.property_unit_id.id,
                    #'sale_line_ids': [(6, 0, [so_line.id])],
                    #'invoice_line_tax_ids': [(6, 0, tax_ids)],
                    #'account_analytic_id': order.project_id.id or False,
                })],
                #'currency_id': order.pricelist_id.currency_id.id,
                #'payment_term_id': order.payment_term_id.id,
                #'fiscal_position_id': order.fiscal_position_id.id or order.partner_id.property_account_position_id.id,
                #'team_id': order.team_id.id,
                'comment': order.notes,
            })
        self.write({'invoice_id':invoice.id})
        self.state = 'booking_fee_created'
        return True

    @api.multi
    def button_create_refund(self):
        self.state = confirm[2][0]

    @api.multi
    def button_create_cancel(self):
        self.state = confirm[2][0]
    
    @api.multi
    def set_draft(self):
        self.state = 'Draft'

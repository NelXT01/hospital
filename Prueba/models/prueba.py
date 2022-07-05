# -*- coding: utf-8 -*-
# importamos el servicio fields para poder crear los campos para guardar los datos de los alumnos
# importamos el servicio models para poder administrar la base de datos donde se guardarán los campos creados
from odoo import api, fields, models, _

# importo un servicio que me permite mostar alertas al usuario cuando sea necesario
from odoo.exceptions import ValidationError
# declaro una clase llamada Alumnos que hereda todas las propiedades de la clase model.Model

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string="Name", required=True, tracking=True)
    reference = fields.Char(string="Reference", required=True, tracking=True, copy=False, readonly=True,
                            default=lambda self:  _('New'))
    age = fields.Integer(string="Age", required=True, tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')], required=True,
                              default='others', tracking=True)
    note = fields.Text(string='Description')
    state = fields.Selection([('draft','Draft'),('confirm','Confirmed'),
                              ('done','Done'),('cancel','Cancelled')],string="Status", default='draft', tracking=True)
    responsible_id = fields.Many2one('res.partner',string="Responsible")

    tiempo2 = fields.Float(string="Hora")

    email_id = fields.Char(string="Email")






    def action_draft(self):
        self.state = 'draft'
    def action_confirm(self):
        self.state = 'confirm'
    def action_done(self):
        self.state = 'done'
    def action_cancel(self):
        self.state = 'cancel'
    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'

        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
            return super(HospitalPatient, self).create(vals)

    def action_send_card(self):
        template_id = self.env.ref('Prueba.patient_card_mail_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
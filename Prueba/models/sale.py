# -*- coding: utf-8 -*-
# importamos el servicio fields para poder crear los campos para guardar los datos de los alumnos
# importamos el servicio models para poder administrar la base de datos donde se guardarán los campos creados
from odoo import api, fields, models, _

# importo un servicio que me permite mostar alertas al usuario cuando sea necesario
from odoo.exceptions import ValidationError
# declaro una clase llamada Alumnos que hereda todas las propiedades de la clase model.Model

class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_description = fields.Char(string="Sale Description")

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Proveedores (models.Model):
    _name = "adquisiciones.proveedores"
    _description = "Detallles de los proveedores"

    nombre = fields.Char(string="Razon social", requiered=True)
    RFC = fields.Char(string="RFC", requiered=True)
    Tipo = fields.Selection([
        ("Proveedores de bienes", "Bienes"),
        ("Proveedores de servicios", "servicios"),
        ("Proveedores de recursos", "recursos")
    ])

    Estatus = fields.Selection([
        ("Activo", "activo"),
        ("Inacticvo", "inactivo")
    ])


# class adquisiciones(models.Model):
#     _name = 'adquisiciones.adquisiciones'
#     _description = 'adquisiciones.adquisiciones'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


# -*- coding: utf-8 -*-
from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not instructors
    conductor = fields.Boolean("Conductor", default=False)

    viaje_ids = fields.Many2many('viajes.viaje', string="Viajes realizados", readonly=True)

# -*- coding: utf-8 -*-
from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not instructors
    conductor = fields.Boolean("Conductor", default=False)

    tarea_ids = fields.Many2many('tareas.tarea', string="Tareas realizadas", readonly=True)


from odoo import models, fields


class Vehiculo(models.Model):
    _name = 'viajes.vehiculo'
    _description = "viajes Vehiculo"
    # char es una frase de una linea
    modelo = fields.Char(string="Modelo", required=True)
    marca = fields.Char(string="Marca")
    # es una cajita más ancha
    descripcion = fields.Text()

    # Con la relación many2one me permite seleccionar un usuario o crearlo directamente
    propietario_id = fields.Many2one('res.users', ondelete='set null', string="Propietario", index=True)

    # En la relacion one2many tengo que crear un coche nuevo al asociarlo
    viaje_ids = fields.One2many('viajes.viaje', 'vehiculo_id', string="Viajes del coche")

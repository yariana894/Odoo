from odoo import models, fields, api


class Viaje(models.Model):
    _name = 'viajes.viaje'
    _description = "Viajes"

    titulo = fields.Char(required=True)
    fecha_inicio = fields.Date(default=fields.Date.today)
    duracion = fields.Float(digits=(6, 2), help="Duracion en días")
    plazas = fields.Integer(string="Numero de plazas disponibles")
    finalizado = fields.Boolean(default=False)

    # En la relación many2one me permite elegir un partner/cliente o crear uno directamente
    # Tener en cuenta que solo aparecerán los partners/clientes que sean de tipo conductor
    conductor_id = fields.Many2one('res.partner', string="Conductor",
                                   domain=['|', ('conductor', '=', True), ('category_id.name', 'ilike',
                                                                           "Conductor")])
    # En la relación many2one me permite elegir un vehiculo o crear uno directamente
    vehiculo_id = fields.Many2one('viajes.vehiculo', ondelete='cascade', string="Vehiculo", required=True)

    # puedo elegir uno(partner/cliente) que ya existe o crear uno nuevo
    pasajeros_ids = fields.Many2many('res.partner', string="Pasajeros")

    plazas_ocupadas = fields.Float(string="Plazas ocupadas", compute='_get_plazas_ocupadas')

    @api.depends('plazas', 'pasajeros_ids')
    def _get_plazas_ocupadas(self):
        for r in self:
            if not r.plazas:
                r.plazas_ocupadas = 0.0
            else:
                r.plazas_ocupadas = 100.0 * len(r.pasajeros_ids) / r.plazas

    @api.onchange('plazas', 'pasajeros_ids')
    def _checkearPlazasValidas(self):
        if self.plazas < 0:
            self.plazas = 0
            return {
                'warning': {
                    'title': "Valor de 'plazas' incorrecto",
                    'message': "El numero de plazas disponibles no puede ser negativo",
                },
            }
        if self.plazas < len(self.pasajeros_ids):
            return {
                'warning': {
                    'title': "Demasiados pasajeros",
                    'message': "Incrementa el nº de plazas o elimina pasajeros",
                },
            }

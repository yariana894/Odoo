from odoo import models, fields, api


class Tareas(models.Model):
    _name = 'tareas.tarea'
    _description = "Tareas"

    titulo = fields.Char(required=True)
    fecha_inicio = fields.Date(default=fields.Date.today)
    duracion = fields.Float(digits=(6, 2), help="Duracion en días")
    plazas = fields.Integer(string="Numero de plazas disponibles")
    finalizado = fields.Boolean(default=False)

    # En la relación many2one me permite elegir un partner/cliente o crear uno directamente
    # Tener en cuenta que solo aparecerán los partners/clientes que sean de tipo conductor
    jefe_id = fields.Many2one('res.partner', string="Jefe", domain=['|', ('conductor', '=', True),
                                                                    ('category_id.name', 'ilike', "Conductor")])

    # En la relación many2one me permite elegir un vehiculo o crear uno directamente
    persona_id = fields.Many2one('tareas.persona', ondelete='cascade', string="Persona", required=True)

    # puedo elegir uno(partner/cliente) que ya existe o crear uno nuevo
    equipos_ids = fields.Many2many('res.partner', string="Equipo")

    plazas_ocupadas = fields.Float(string="Plazas ocupadas", compute='_get_plazas_ocupadas')

    @api.depends('plazas', 'equipos_ids')
    def _get_plazas_ocupadas(self):
        for r in self:
            if not r.plazas:
                r.plazas_ocupadas = 0.0
            else:
                r.plazas_ocupadas = 100.0 * len(r.equipos_ids) / r.plazas

    @api.onchange('plazas', 'equipos_ids')
    def _checkearPlazasValidas(self):
        if self.plazas < 0:
            self.plazas = 0
            return {
                'warning': {
                    'title': "Valor de 'plazas' incorrecto",
                    'message': "El numero de plazas disponibles no puede ser negativo",
                },
            }
        if self.plazas < len(self.equipos_ids):
            return {
                'warning': {
                    'title': "Demasiados pasajeros",
                    'message': "Incrementa el nº de plazas o elimina pasajeros",
                },
            }

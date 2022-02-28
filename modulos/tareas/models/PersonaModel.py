from odoo import models, fields


class Persona(models.Model):
    _name = 'tareas.persona'
    _description = "tareas Persona"
    nombre = fields.Char(string="Nombre", required=True)
    asignatura = fields.Char(string="Asignatura")
    descripcion = fields.Text()

    # Con la relación many2one me permite seleccionar un usuario o crearlo directamente
    empleado_id = fields.Many2one('res.users',
                                  ondelete='set null', string="Empleado", index=True)

    # En la relacion one2many tengo que crear un coche nuevo al asociarlo
    tarea_ids = fields.One2many('tareas.tarea', 'persona_id', string="Tareas de la persona")

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class UserTask(models.Model):
    _name = "user.task"              # Nombre técnico del modelo en Odoo (tabla lógica)
    _description = "User Task"       # Descripción legible del modelo
    _order = 'deadline asc'          # Orden por defecto: primero las tareas con fecha límite más próxima

    # Campos básicos de la tarea
    name = fields.Char(
        string='Titulo',             # Etiqueta que verá el usuario en la interfaz
        required=True                # Campo obligatorio
    )
    description = fields.Text(       # Campo de texto largo para detalles de la tarea
        string='Descripción'
    )

    # Prioridad de la tarea: baja, media, alta
    priority = fields.Selection(
        [('0', 'Baja'), ('1', 'Media'), ('2', 'Alta')],
        string='Prioridad',
        default='1',                 # Por defecto, prioridad media
        required=True
    )

    # Estado del flujo de la tarea
    state = fields.Selection(
        [
            ("draft", "Borrador"),       # Tarea recién creada
            ("in_progress", "En Progreso"),  # Tarea en ejecución
            ("done", "Completada")       # Tarea finalizada
        ],
        string="Estado",
        default="draft",              # Por defecto, empieza en borrador
    )

    # Fecha límite para completar la tarea
    deadline = fields.Date(
        string="Fecha Límite"
    )

    # Campo calculado para marcar si está completada
    is_done = fields.Boolean(
        string="Completada",
        compute="_compute_is_done",   # Método que calcula el valor
        store=True                    # Se guarda en base de datos
    )

    # Usuario al que se asigna la tarea
    user_id = fields.Many2one(
        "res.users",                  # Relación con el modelo de usuarios de Odoo
        string="Asignado a",
        default=lambda self: self.env.user,  # Por defecto, el usuario actual
        required=True,
    )

    @api.depends("state")             # Odoo recalculará is_done cuando cambie el estado
    def _compute_is_done(self):
        for record in self:
            # Marca como completada si el estado es "done"
            record.is_done = record.state == "done"

    @api.constrains("deadline")       # Restricción de validación sobre el campo deadline
    def _check_deadline(self):
        for task in self:
            # Si hay fecha límite, no puede ser anterior al día de hoy
            if task.deadline and task.deadline < fields.Date.today():
                raise ValidationError(
                    "La fecha límite no puede ser anterior a hoy"
                )

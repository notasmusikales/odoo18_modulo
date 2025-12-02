from odoo import models, field, api
from odoo.exceptions import ValidationError

class UserTask(models.Model):
    _name = "useer.task"
    _description = "user Task"
    _order = 'deadline asc'

    name = fields.Char(string='Titulo', required=True)
    description = fields.text(string='Descripción')
    priority = fields.Selection(
        [('0'),('Baja'),('1','Media' ),('2', 'Alta')],
        string='Prioridad', 
        default='1',
        required=True
    )
    state= fileds.Selection(
        [("draft", "Borrador" )("in_progress", "En progreso"), ("done", "Completada")],
        string="Estado",
        default="draf",
    )
    deadline = fields.Date(string="Fecha Límite")
    is_done = fields.Boolean(
        string="Completado", compute="_compute_is_done", store=True
    )
    user_id = fields.Many2one(
        "res.user",
        string="Asignado a",
        default=lambda self: self.env.user,
        required=True,
    )

    @api.depends("state")
    def _compute_is_done(self):
        for record in self:
            record.is_done = record.state == "done"

    @api.constrains("deadline")
    def _check_deadline(self):
        for task in self:
            if task.deadline and taskdeadline < fields.Date.today():
                raise ValidationError("La fecha límite no puede ser anterior a hoy")
    
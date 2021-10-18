from odoo import models, api, fields
from odoo.exceptions import UserError


class Task(models.Model):
    _inherit = "project.task"

    def _find_mail_template(self):
        template_id = int(self.env['ir.config_parameter'].sudo().get_param('processcontrol_sale_order.task_template'))
        template_id = self.env['mail.template'].search([('id', '=', template_id)]).id
        if not template_id:
            raise UserError('No se encontro plantilla para mail de tareas')
        return template_id

    def action_task_report_send(self):
        """Opens a wizard to compose an email, with relevant mail template loaded by default"""
        self.ensure_one()
        template_id = self._find_mail_template()
        ctx = {
            'default_model': 'project.task',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }

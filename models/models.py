# -*- coding: utf-8 -*-

from odoo import models, fields, api


class projectreports(models.Model):
    # _inherit = 'project.project'
    _name = 'report.projectreports.projectreports'
    _description = 'projectreports.projectreports'




    @api.model
    def _get_report_values(self, docids, data):
        mes_reporte = data['mes']

        record = self._cr.dictfetchall()
        return {
            'docs': record,
            'mes_report': mes_reporte,
        }

class imagenreport(models.Model):
    
    _name = 'projectreports.imagenreport'
    _description = 'Imagenes para subir al reporte'

    name = fields.Char(string="Descripción de la imagen")
    picture = fields.Binary(string="Imagen")
    
    mes_imagen = fields.Selection(string = 'Mes', default='1',
                        selection=[('1', 'Enero'),
                                    ('2', 'Febrero'),
                                    ('3', 'Marzo'),
                                    ('4', 'Abril'),
                                    ('5', 'Mayo'),
                                    ('6', 'Junio'),
                                    ('7', 'Julio'),
                                    ('8', 'Agosto'),
                                    ('9', 'Septiembre'),
                                    ('10', 'Octubre'),
                                    ('11', 'Noviembre'),
                                    ('12', 'Diciembre')])
 
    projecto_id = fields.Many2one('project.project',
       ondelete='cascade', string="Projecto", required=True)

class project(models.Model):
    _inherit = 'project.project'

    month_tdisp = fields.Integer()
    imagenes = fields.One2many('projectreports.imagenreport', 'projecto_id', string="Imagenes: ")


# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class projectreports(models.Model):
    # _inherit = 'project.project'
    _name = 'projectreports.projectreports'
    _description = 'projectreports.projectreports'
    # _order = "sequence,id"
    



    @api.model
    def _get_report_values(self, docids, data):
        # mes_reporte = data['mes']
        # año_reporte = data['año']
        intr_reporte = data['intr']
        fecha1_reporte = data['fecha1']
        fecha2_reporte = data['fecha2']

        record = self._cr.dictfetchall()
        
        # /*
        #     'mes_report': mes_reporte,
        #     'año_report': año_reporte, */

        return {
            'docs': record, 
            'intr_report': intr_report,
            'fecha1_report': fecha1_reporte,
            'fecha2_report': fecha2_reporte,
        }

class imagenreport(models.Model):
    
    _name = 'projectreports.imagenreport'
    _description = 'Imagenes para subir al reporte'

    _order = "sequence,fecha_img,id"
    sequence = fields.Integer('sequence', help="Sequence for the handle.",default=10)

    name = fields.Char(string="Descripción de la imagen")
    picture = fields.Binary(string="Imagen")
    
    fecha_img = fields.Date(string="Fecha de la imagen")

    # mes_imagen = fields.Selection(string = 'Mes', default='1',
    #                     selection=[('1', 'Enero'),
    #                                 ('2', 'Febrero'),
    #                                 ('3', 'Marzo'),
    #                                 ('4', 'Abril'),
    #                                 ('5', 'Mayo'),
    #                                 ('6', 'Junio'),
    #                                 ('7', 'Julio'),
    #                                 ('8', 'Agosto'),
    #                                 ('9', 'Septiembre'),
    #                                 ('10', 'Octubre'),
    #                                 ('11', 'Noviembre'),
    #                                 ('12', 'Diciembre')])


    # def _get_years(self):
    #     year_list = []
    #     x = datetime.datetime.now()
    #     for i in range(2018, x.year+1):
    #         year_list.append((i, str(i)))
    #     return year_list

    # año_imagen = fields.Selection(_get_years, string='Año', required=True)
    # año_imagen = fields.Integer(string="Año", default='2020', required=True)

    projecto_id = fields.Many2one('project.project',
       ondelete='cascade', string="Projecto", required=True)

class project(models.Model):
    _inherit = 'project.project'

    # month_tdisp = fields.Integer()
    # year_tdisp = fields.Integer()

    fecha_ini = fields.Date()
    fecha_end = fields.Date()

    intro = fields.Text()

    imagenes = fields.One2many('projectreports.imagenreport', 'projecto_id', string="Imagenes: ")


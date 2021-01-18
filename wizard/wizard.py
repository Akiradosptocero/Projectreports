# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging, datetime
_logger = logging.getLogger(__name__)

class Wizard(models.TransientModel):
    _name = 'projectreports.wizard'
    _description = "Wizard: Preguntar el mes para realizar reporte del proyecto"
    

    def _get_default_projects(self):
        return self.env['project.project'].browse(self.env.context.get('active_ids'))


    def hacer_reporte_mes(self):
        return self.env['project.project'].browse(self.env.context.get('active_ids'))

    # def _get_years(self):
    #     year_list = []
    #     x = datetime.datetime.now()
    #     for i in range(x.year-1, x.year+1):
    #         year_list.append((i, str(i)))
    #     return year_list


    projects_ids = fields.Many2many('project.project', string='Project', default=_get_default_projects)
    

    # def _get_default_imagen_order_ids(self):
    #     return self.env['project.project'].search([('projecto_id','in','projects_ids')])
    # , default=_get_default_imagen_order_ids
    imagenes_ids = fields.Many2many('projectreports.imagenreport', string='Orden Imagenes')

    # mes_report = fields.Selection(string = 'Mes', default='1',
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

    # año_report = fields.Selection(_get_years, string='Año', required=True)
    introduccion = fields.Text(string="Introduccion")

    date1 = fields.Date(string="Fecha comienzo")
    date2 = fields.Date(string="Fecha de fin")

    # año_report = fields.Integer(string = "Año", default='2020')

    # def tarea_mes_seleccionado(self, mes):
    #         mes_tarea = tarea.date # sacar mes y pasar a int
    #         if mes_tarea == mes:
    #             return True
 
    # def filtrar_mes(self, tareas):
    #     tareas_mes = filter(tarea_mes_seleccionado, tareas)
    #     return 

    def filtrar_mes(self): 
        
        # /*
        #     'mes': self.mes_report,
        #     'año': self.año_report, */
        data = {
            'docs': self.projects_ids,
            'intr': self.introduccion,
            'fecha1': self.date1,
            'fecha2': self.date2,
        }
        _logger.info(self.projects_ids.mapped('id'))                              
        
                                                                                    # /*'month_tdisp': int(self.mes_report),
                                                                                    # 'year_tdisp': int(self.año_report), */

        self.env['project.project'].browse(self.projects_ids.mapped('id')).write({'intro': str(self.introduccion),
                                                                                    'fecha_ini': str(self.date1),
                                                                                    'fecha_end': str(self.date2)})
        # _logger.info(self.env.context)
        # self.with_context(mes=self.mes_report)
        # self.env.context.update({'mes': self.mes_report})

        return self.env.ref('projectreports.action_report_project').report_action(self.projects_ids.mapped('id'))
        # report = self.env.ref('projectreports.action_report_project')
        # report_action = {
        #     'context': self.env.context,
        #     'data': {},
        #     'type': 'ir.actions.report',
        #     'report_name': report.report_name,
        #     'report_type': report.report_type,
        #     'report_file': report.report_file,
        #     'name': report.name,
        # }
        # _logger.info(str(report_action))
        # return report_action
        #return self.env.ref('stock.action_report_stock_rule').report_action(None, data=data)
    #https://www.cybrosys.com/blog/how-to-create-pdf-report-odoo-13
        # return Report.render('projectreports.action_report_project', datos_reporte)

    # @api.multi    
    # def print_report1(self):
    #     context = self._context        
    #     obj = self.env['stock.pack.operation'].search([('id', '=', context.get('product_id'))])                
    #     self.product_name = obj.product_id.name       
    #     self.product_barcode = obj.product_id.barcode           
    #     if obj.product_id.barcode:
    #         return self.env['report'].get_action(self, 'print_barcode.report_barcode')           
    #     else:
    #         raise Warning((_("Please set barcode for the product %s") % obj.product_id.name))

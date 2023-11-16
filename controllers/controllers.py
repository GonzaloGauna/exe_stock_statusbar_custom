# -*- coding: utf-8 -*-
# from odoo import http


# class ExeStockStatusbarCustom(http.Controller):
#     @http.route('/exe_stock_statusbar_custom/exe_stock_statusbar_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exe_stock_statusbar_custom/exe_stock_statusbar_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exe_stock_statusbar_custom.listing', {
#             'root': '/exe_stock_statusbar_custom/exe_stock_statusbar_custom',
#             'objects': http.request.env['exe_stock_statusbar_custom.exe_stock_statusbar_custom'].search([]),
#         })

#     @http.route('/exe_stock_statusbar_custom/exe_stock_statusbar_custom/objects/<model("exe_stock_statusbar_custom.exe_stock_statusbar_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exe_stock_statusbar_custom.object', {
#             'object': obj
#         })

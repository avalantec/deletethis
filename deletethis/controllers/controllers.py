# -*- coding: utf-8 -*-
# from odoo import http


# class Deletethis(http.Controller):
#     @http.route('/deletethis/deletethis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/deletethis/deletethis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('deletethis.listing', {
#             'root': '/deletethis/deletethis',
#             'objects': http.request.env['deletethis.deletethis'].search([]),
#         })

#     @http.route('/deletethis/deletethis/objects/<model("deletethis.deletethis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('deletethis.object', {
#             'object': obj
#         })

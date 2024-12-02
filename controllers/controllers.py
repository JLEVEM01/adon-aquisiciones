# -*- coding: utf-8 -*-
# from odoo import http


# class Adquisiciones(http.Controller):
#     @http.route('/adquisiciones/adquisiciones', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/adquisiciones/adquisiciones/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('adquisiciones.listing', {
#             'root': '/adquisiciones/adquisiciones',
#             'objects': http.request.env['adquisiciones.adquisiciones'].search([]),
#         })

#     @http.route('/adquisiciones/adquisiciones/objects/<model("adquisiciones.adquisiciones"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('adquisiciones.object', {
#             'object': obj
#         })


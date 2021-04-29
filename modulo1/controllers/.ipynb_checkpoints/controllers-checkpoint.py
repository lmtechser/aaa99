# -*- coding: utf-8 -*-
from odoo import http


class Modulo1(http.Controller):
     @http.route('/modulo1/modulo1/', auth='public')
     def index(self, **kw):
         return "Hello, world"

        
     @http.route('/modulo1/modulo1/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('modulo1.listing', {
             'root': '/modulo1/modulo1',
             'objects': http.request.env['modulo1.modulo1'].search([]),
         })

     @http.route('/modulo1/modulo1/objects/<model("modulo1.modulo1"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('modulo1.object', {
             'object': obj
         })

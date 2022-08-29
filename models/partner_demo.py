# -*- coding: utf-8 -*-

from odoo import fields, models


class PartnerDemo(models.Model):
    _name = 'res.partner.demo1'
    _description = "Partner Demo 1"
    # _table = 'partner_demo1' # if you can set user define table name then use this
    # _order = 'name asc' # if you can set user define order by then use this one

    name = fields.Char(string='Name', help='Name Of The Partner.')
    email = fields.Char(string='Email')
    phone_no = fields.Char(string='Phone No')
    gender = fields.Selection(selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')])
    last_name = fields.Char(string='Last Name', help='Last Name Of The Partner.')

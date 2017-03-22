# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Mail digest',
    'summary': """Basic digest mail handling.""",
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Camptocamp,Odoo Community Association (OCA)',
    'depends': [
        'mail',
    ],
    'data': [
        'data/ir_cron.xml',
        # TODO: fix permissions (only admin now)
        'security/ir.model.access.csv',
        'views/mail_digest_views.xml',
        'views/partner_views.xml',
        'views/user_views.xml',
        'templates/digest_default.xml',
    ],
}

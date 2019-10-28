# -*- coding: utf-8 -*-


from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSaleForm


class ExtraStepNote(WebsiteSaleForm):

    @http.route()
    def website_form_saleorder(self, **kwargs):
        order = http.request.website.sale_get_order()
        order.note += "\n\n%s" % kwargs['Give us your feedback...']

        return super(ExtraStepNote, self).website_form_saleorder()

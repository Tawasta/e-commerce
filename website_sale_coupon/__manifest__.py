# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2017 Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

{
    'name': 'Website sale coupons',
    'summary': 'Discount coupons for website',
    'version': '10.0.0.16.3',
    'category': 'Website',
    'website': 'http://www.tawasta.fi',
    'author': 'Oy Tawasta Technologies Ltd.',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'depends': [
        'website_sale',
    ],
    'data': [
        'data/product_product.xml',
        'security/ir.model.access.csv',

        'views/website_sale_coupon_form.xml',
        'views/website_sale_coupon_log_tree.xml',
        'views/website_sale_coupon_menu.xml',
        'views/website_sale_coupon_tree.xml',
        'views/website_template_coupon.xml',
        'views/website_template_coupon_assets.xml',
        'views/website_template_sale_address.xml',
        'views/website_template_sale_cart.xml',
        'views/website_template_sale_payment.xml',
    ],
    'demo': [
    ],
}

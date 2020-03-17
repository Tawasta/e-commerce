##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2019 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
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
    'name': 'eCommerce Delivery cost with tax',
    'summary': 'Website sale delivery costs with tax',
    'version': '12.0.1.0.0',
    'category': 'Website',
    'website': 'https://github.com/Tawasta/e-commerce',
    'author': 'Tawasta',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'delivery',
        'delivery_carrier_price_with_tax',
        'website_sale_delivery',
    ],
    'data': [
        'views/website_payment_delivery_methods.xml',
    ],
}

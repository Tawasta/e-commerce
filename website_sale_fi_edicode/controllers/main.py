##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2018- Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
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


# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
# from odoo import http
# from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

# 4. Imports from Odoo modules (rarely, and only if necessary):

# 5. Local imports in the relative form:

# 6. Unknown third party imports (One per line sorted and splitted in


class WebsiteSale(WebsiteSale):

    def _checkout_form_save(self, mode, checkout, all_values):
        """
        Add edicode and operator to saved values
        """
        is_company = all_values.get('is_company', False)
        edicode = all_values.get('edicode', False)
        einvoice_operator = all_values.get('einvoice_operator', False)
        checkout['edicode'] = edicode if is_company else ''
        checkout['einvoice_operator'] = einvoice_operator if is_company else ''
        return super(WebsiteSale, self)\
            ._checkout_form_save(mode, checkout, all_values)

odoo.define('website_sale_company_slider.checkout', function (require) {
    "use strict";

    var _t = require('web.core')._t;

    $(function() {

        const REQUIRED_FIELDS_DEFAULT = $("input[name='field_required']").val();
        const FI_COUNTRY_ID = $('#fi_country_id').val();

        function showFields() {
            var is_company = $('#is_company').is(':checked');
            var required_fields = $("input[name='field_required']");
            // Reset required fields set
            required_fields.val(REQUIRED_FIELDS_DEFAULT);
            if (is_company === true) {
                $("label[for='company_name']").removeClass('label-optional');
                $("label[id='is_company_label_true']").addClass('text-success');
                $("label[id='is_company_label_false']").removeClass('text-success');
                $("label[for='vat']").removeClass('label-optional');
                $('#is_company').attr('checked', 'checked');
                if (required_fields.val().indexOf(',company_name,vat') < 0) {
                    required_fields.val(required_fields.val() + ',company_name,vat');
                }
                $('.show-company').show();
                $('.hide-company').hide();
            } else {
                $("label[for='company_name']").addClass('label-optional');
                $("label[id='is_company_label_false']").addClass('text-success');
                $("label[id='is_company_label_true']").removeClass('text-success');
                $("label[for='vat']").addClass('label-optional');
                $('#is_company').removeAttr('checked');
                $('.show-company').hide();
                $('.hide-company').show();
                required_fields.val(required_fields.val().replace(',company_name,vat', ''));
            }
            console.log(required_fields.val());
        }
        showFields();
        $('#is_company').click(function() {
            showFields();
        });

        $('.oe_website_sale .a-submit, #comment .a-submit').off('click').on('click', function (event) {
            if (!event.isDefaultPrevented() && !$(this).is(".disabled")) {
                var form = $(this).closest('form');
                var is_company = $('#is_company').is(':checked');
                if (is_company === false) {
                    // Empty company related fields
                    $('.show-company').val('');
                    $('input[name="vat"]').val('');
                }
                // If country is Finland and VAT is inserted, make business id
                var vat = $(form).find("input[name='vat']").val();
                var country_id = $('#country_id').val();

                if (vat && country_id === FI_COUNTRY_ID) {
                    var parsed = vat.replace(/[^0-9]/g, '');
                    var business_id = parsed.substr(0, 7) + '-' + parsed.substr(7, 1);
                    $(form).append('<input type="hidden" name="business_id" value="' + business_id + '"/>');
                }
                $(this).closest('form').submit();
            }
            if ($(this).hasClass('a-submit-disable')){
                $(this).addClass("disabled");
            }
            if ($(this).hasClass('a-submit-loading')){
                var loading = '<span class="fa fa-cog fa-spin"/>';
                var fa_span = $(this).find('span[class*="fa"]');
                if (fa_span.length){
                    fa_span.replaceWith(loading);
                }
                else{
                    $(this).append(loading);
                }
            }
        });
    });
});
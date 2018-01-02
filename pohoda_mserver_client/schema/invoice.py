# Copyright (C) 2018 Pohoda-mserver-client authors. See the AUTHORS file found
# in the top-level directory of this distribution.
#
# Licensed under the MIT (Expat) License. See the LICENSE file found in the
# top-level directory of this distribution.

import pohoda_mserver_client.schema.type
import pohoda_mserver_client.schema.xsd


URI = 'http://www.stormware.cz/schema/version_2/invoice.xsd'


def load_invoice_type(invoice_type_dump):
    if invoice_type_dump.get('version') != '2.0':
        raise ValueError()
    if invoice_type_dump.find(f'{{{URI}}}links') is not None:
        raise ValueError()
    if invoice_type_dump.find(f'{{{URI}}}cancelDocument') is not None:
        raise ValueError()
    if invoice_type_dump.find(f'{{{URI}}}print') is not None:
        raise ValueError()
    if invoice_type_dump.find(f'{{{URI}}}EET') is not None:
        raise ValueError()

    header = None
    header_dump = invoice_type_dump.find(f'{{{URI}}}invoiceHeader')
    if header_dump is not None:
        header = load_invoice_header_type(header_dump)

    items = None
    invoice_detail_dump = invoice_type_dump.find(f'{{{URI}}}invoiceDetail')
    if invoice_detail_dump is not None:
        items = load_invoice_detail_type(invoice_detail_dump)

    summary = None
    invoice_summary_dump = invoice_type_dump.find(f'{{{URI}}}invoiceSummary')
    if invoice_summary_dump is not None:
        summary = load_invoice_summary_type(invoice_summary_dump)

    return InvoiceType(header, items, summary)


def load_invoice_detail_type(invoice_detail_type_dump):
    if invoice_detail_type_dump.find(f'{{{URI}}}invoiceAdvancePaymentItem') is not None:
        raise ValueError()

    items_dumps = invoice_detail_type_dump.iterfind(f'{{{URI}}}invoiceItem')
    items = (load_invoice_item_type(item_dump) for item_dump in items_dumps)

    return items


def load_invoice_header_type(invoice_header_type_dump):
    if invoice_header_type_dump.find(f'{{{URI}}}extId') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}storno') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}sphereType') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}order') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}numberOrder') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}dateOrder') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}paymentAccount') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}paymentTerminal') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}centre') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}activity') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}contract') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}regVATinEU') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}MOSS') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}evidentiaryResourcesMOSS') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}accountingPeriodMOSS') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}carrier') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}labels') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}intrastat') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}parameters') is not None:
        raise ValueError()
    if invoice_header_type_dump.find(f'{{{URI}}}validate') is not None:
        raise ValueError()

    id_ = None
    id_dump = invoice_header_type_dump.find(f'{{{URI}}}id')
    if id_dump is not None:
        id_ = pohoda_mserver_client.schema.type.load_id_type(id_dump)

    type_ = None
    type_dump = invoice_header_type_dump.find(f'{{{URI}}}invoiceType')
    if type_dump is not None:
        type_ = load_invoice_type_type(type_dump)

    number = None
    number_dump = invoice_header_type_dump.find(f'{{{URI}}}number')
    if number_dump is not None:
        number = pohoda_mserver_client.schema.type.load_number_type(number_dump)

    sym_var = None
    sym_var_dump = invoice_header_type_dump.find(f'{{{URI}}}symVar')
    if sym_var_dump is not None:
        sym_var = pohoda_mserver_client.schema.type.load_sym_var_type(sym_var_dump)

    original_document = None
    original_document_dump = invoice_header_type_dump.find(f'{{{URI}}}originalDocument')
    if original_document_dump is not None:
        original_document = pohoda_mserver_client.schema.type.load_document_number_type(original_document_dump)

    original_document_number = None
    original_document_number_dump = invoice_header_type_dump.find(f'{{{URI}}}originalDocumentNumber')
    if original_document_number_dump is not None:
        original_document_number = pohoda_mserver_client.schema.xsd.load_string(original_document_number_dump)

    sym_par = None
    sym_par_dump = invoice_header_type_dump.find(f'{{{URI}}}symPar')
    if sym_par_dump is not None:
        sym_par = pohoda_mserver_client.schema.type.load_sym_var_type(sym_par_dump)

    date = None
    date_dump = invoice_header_type_dump.find(f'{{{URI}}}date')
    if date_dump is not None:
        date = pohoda_mserver_client.schema.xsd.load_date(date_dump)

    date_tax = None
    date_tax_dump = invoice_header_type_dump.find(f'{{{URI}}}dateTax')
    if date_tax_dump is not None:
        date_tax = pohoda_mserver_client.schema.xsd.load_date(date_tax_dump)

    date_accounting = None
    date_accounting_dump = invoice_header_type_dump.find(f'{{{URI}}}dateAccounting')
    if date_accounting_dump is not None:
        date_accounting = pohoda_mserver_client.schema.xsd.load_date(date_accounting_dump)

    date_khdph = None
    date_khdph_dump = invoice_header_type_dump.find(f'{{{URI}}}dateKHDPH')
    if date_khdph_dump is not None:
        date_khdph = pohoda_mserver_client.schema.xsd.load_date(date_khdph_dump)

    date_due = None
    date_due_dump = invoice_header_type_dump.find(f'{{{URI}}}dateDue')
    if date_due_dump is not None:
        date_due = pohoda_mserver_client.schema.xsd.load_date(date_due_dump)

    date_application_vat = None
    date_application_vat_dump = invoice_header_type_dump.find(f'{{{URI}}}dateApplicationVAT')
    if date_application_vat_dump is not None:
        date_application_vat = pohoda_mserver_client.schema.xsd.load_date(date_application_vat_dump)

    date_delivery = None
    date_delivery_dump = invoice_header_type_dump.find(f'{{{URI}}}dateDelivery')
    if date_delivery_dump is not None:
        date_delivery = pohoda_mserver_client.schema.xsd.load_date(date_delivery_dump)

    accounting = None
    accounting_dump = invoice_header_type_dump.find(f'{{{URI}}}accounting')
    if accounting_dump is not None:
        accounting = pohoda_mserver_client.schema.type.load_accounting_type(accounting_dump)

    classification_vat = None
    classification_vat_dump = invoice_header_type_dump.find(f'{{{URI}}}classificationVAT')
    if classification_vat_dump is not None:
        classification_vat = pohoda_mserver_client.schema.type.load_classification_vat_type(classification_vat_dump)

    classification_kvdph = None
    classification_kvdph_dump = invoice_header_type_dump.find(f'{{{URI}}}classificationKVDPH')
    if classification_kvdph_dump is not None:
        classification_kvdph = pohoda_mserver_client.schema.type.load_ref_type(classification_kvdph_dump)

    number_khdph = None
    number_khdph_dump = invoice_header_type_dump.find(f'{{{URI}}}numberKHDPH')
    if number_khdph_dump is not None:
        number_khdph = pohoda_mserver_client.schema.type.load_string32(number_khdph_dump)

    number_kvdph = None
    number_kvdph_dump = invoice_header_type_dump.find(f'{{{URI}}}numberKVDPH')
    if number_kvdph_dump is not None:
        number_kvdph = pohoda_mserver_client.schema.type.load_string32(number_kvdph_dump)

    text = None
    text_dump = invoice_header_type_dump.find(f'{{{URI}}}text')
    if text_dump is not None:
        text = pohoda_mserver_client.schema.type.load_string240(text_dump)

    partner_identity = None
    partner_identity_dump = invoice_header_type_dump.find(f'{{{URI}}}partnerIdentity')
    if partner_identity_dump is not None:
        partner_identity = pohoda_mserver_client.schema.type.load_address(partner_identity_dump)

    my_identity = None
    my_identity_dump = invoice_header_type_dump.find(f'{{{URI}}}myIdentity')
    if my_identity_dump is not None:
        my_identity = pohoda_mserver_client.schema.type.load_my_address(my_identity_dump)

    price_level = None
    price_level_dump = invoice_header_type_dump.find(f'{{{URI}}}priceLevel')
    if price_level_dump is not None:
        price_level = pohoda_mserver_client.schema.type.load_ref_type(price_level_dump)

    payment_type = None
    payment_type_dump = invoice_header_type_dump.find(f'{{{URI}}}paymentType')
    if payment_type_dump is not None:
        payment_type = pohoda_mserver_client.schema.type.load_payment_type(payment_type_dump)

    sym_const = None
    sym_const_dump = invoice_header_type_dump.find(f'{{{URI}}}symConst')
    if sym_const_dump is not None:
        sym_const = pohoda_mserver_client.schema.xsd.load_string(sym_const_dump)

    sym_spec = None
    sym_spec_dump = invoice_header_type_dump.find(f'{{{URI}}}symSpec')
    if sym_spec_dump is not None:
        sym_spec = pohoda_mserver_client.schema.xsd.load_string(sym_spec_dump)

    note = None
    note_dump = invoice_header_type_dump.find(f'{{{URI}}}note')
    if note_dump is not None:
        note = pohoda_mserver_client.schema.xsd.load_string(note_dump)

    int_note = None
    int_note_dump = invoice_header_type_dump.find(f'{{{URI}}}intNote')
    if int_note_dump is not None:
        int_note = pohoda_mserver_client.schema.xsd.load_string(int_note_dump)

    liquidation = None
    liquidation_dump = invoice_header_type_dump.find(f'{{{URI}}}liquidation')
    if liquidation_dump is not None:
        liquidation = pohoda_mserver_client.schema.type.load_liquidation_type(liquidation_dump)

    mark_record = 'true'
    mark_record_dump = invoice_header_type_dump.find(f'{{{URI}}}markRecord')
    if mark_record_dump is not None:
        mark_record = pohoda_mserver_client.schema.type.load_boolean(mark_record_dump)

    return InvoiceHeaderType(id_, type_, number, sym_var, original_document, original_document_number, sym_par, date, date_tax, date_accounting, date_khdph, date_due, date_application_vat, date_delivery, accounting, classification_vat, classification_kvdph, number_khdph, number_kvdph, text, partner_identity, my_identity, price_level, payment_type, sym_const, sym_spec, note, int_note, liquidation, mark_record)


def load_invoice_item_type(invoice_item_type_dump):
    if invoice_item_type_dump.find(f'{{{URI}}}link') is not None:
        raise ValueError()
    if invoice_item_type_dump.find(f'{{{URI}}}typeServiceMOSS') is not None:
        raise ValueError()
    if invoice_item_type_dump.find(f'{{{URI}}}code') is not None:
        raise ValueError()
    if invoice_item_type_dump.find(f'{{{URI}}}guarantee') is not None:
        raise ValueError()
    if invoice_item_type_dump.find(f'{{{URI}}}guaranteeType') is not None:
        raise ValueError()
    if invoice_item_type_dump.find(f'{{{URI}}}stockItem') is not None:
        raise ValueError()
    if invoice_item_type_dump.find(f'{{{URI}}}centre') is not None:
        raise ValueError()
    if invoice_item_type_dump.find(f'{{{URI}}}activity') is not None:
        raise ValueError()
    if invoice_item_type_dump.find(f'{{{URI}}}contract') is not None:
        raise ValueError()
    if invoice_item_type_dump.find(f'{{{URI}}}expirationDate') is not None:
        raise ValueError()
    if invoice_item_type_dump.find(f'{{{URI}}}intrastatItem') is not None:
        raise ValueError()
    if invoice_item_type_dump.find(f'{{{URI}}}EETItem') is not None:
        raise ValueError()
    if invoice_item_type_dump.find(f'{{{URI}}}parameters') is not None:
        raise ValueError()

    id_ = None
    id_dump = invoice_item_type_dump.find(f'{{{URI}}}id')
    if id_dump is not None:
        id_ = pohoda_mserver_client.schema.type.load_id_type(id_dump)

    text = None
    text_dump = invoice_item_type_dump.find(f'{{{URI}}}text')
    if text_dump is not None:
        text = pohoda_mserver_client.schema.type.load_string90(text_dump)

    quantity = None
    quantity_dump = invoice_item_type_dump.find(f'{{{URI}}}quantity')
    if quantity_dump is not None:
        quantity = pohoda_mserver_client.schema.xsd.load_float(quantity_dump)

    unit = None
    unit_dump = invoice_item_type_dump.find(f'{{{URI}}}unit')
    if unit_dump is not None:
        unit = pohoda_mserver_client.schema.type.load_unit_type(unit_dump)

    coefficient = 1.0
    coefficient_dump = invoice_item_type_dump.find(f'{{{URI}}}coefficient')
    if coefficient_dump is not None:
        coefficient = pohoda_mserver_client.schema.xsd.load_float(coefficient_dump)

    pay_vat = 'false'
    pay_vat_dump = invoice_item_type_dump.find(f'{{{URI}}}payVAT')
    if pay_vat_dump is not None:
        pay_vat = pohoda_mserver_client.schema.type.load_boolean(pay_vat_dump)

    rate_vat = 'none'
    rate_vat_dump = invoice_item_type_dump.find(f'{{{URI}}}rateVAT')
    if rate_vat_dump is not None:
        rate_vat = pohoda_mserver_client.schema.type.load_vat_rate_type(rate_vat_dump)

    percent_vat = None
    percent_vat_dump = invoice_item_type_dump.find(f'{{{URI}}}percentVAT')
    if percent_vat_dump is not None:
        percent_vat = pohoda_mserver_client.schema.xsd.load_float(percent_vat_dump)

    discount_percentage = 0.0
    discount_percentage_dump = invoice_item_type_dump.find(f'{{{URI}}}discountPercentage')
    if discount_percentage_dump is not None:
        discount_percentage = pohoda_mserver_client.schema.type.load_type_percentage(discount_percentage_dump)

    home_currency = None
    home_currency_dump = invoice_item_type_dump.find(f'{{{URI}}}homeCurrency')
    if home_currency_dump is not None:
        home_currency = pohoda_mserver_client.schema.type.load_type_currency_home_item(home_currency_dump)

    foreign_currency = None
    foreign_currency_dump = invoice_item_type_dump.find(f'{{{URI}}}foreignCurrency')
    if foreign_currency_dump is not None:
        foreign_currency = pohoda_mserver_client.schema.type.load_type_currency_foreign_item(foreign_currency_dump)

    note = None
    note_dump = invoice_item_type_dump.find(f'{{{URI}}}note')
    if note_dump is not None:
        note = pohoda_mserver_client.schema.type.load_string90(note_dump)

    accounting = None
    accounting_dump = invoice_item_type_dump.find(f'{{{URI}}}accounting')
    if accounting_dump is not None:
        accounting = pohoda_mserver_client.schema.type.load_ref_type(accounting_dump)

    classification_vat = None
    classification_vat_dump = invoice_item_type_dump.find(f'{{{URI}}}classificationVAT')
    if classification_vat_dump is not None:
        classification_vat = pohoda_mserver_client.schema.type.load_classification_vat_type(classification_vat_dump)

    classification_kvdph = None
    classification_kvdph_dump = invoice_item_type_dump.find(f'{{{URI}}}classificationKVDPH')
    if classification_kvdph_dump is not None:
        classification_kvdph = pohoda_mserver_client.schema.type.load_ref_type(classification_kvdph_dump)

    return InvoiceItemType(id_, text, quantity, unit, coefficient, pay_vat, rate_vat, percent_vat, discount_percentage, home_currency, foreign_currency, note, accounting, classification_vat, classification_kvdph)


def load_invoice_summary_type(invoice_summary_type_dump):
    rounding_document = None
    rounding_document_dump = invoice_summary_type_dump.find(f'{{{URI}}}roundingDocument')
    if rounding_document_dump is not None:
        rounding_document = pohoda_mserver_client.schema.type.load_type_rounding_document(rounding_document_dump)

    rounding_vat = None
    rounding_vat_dump = invoice_summary_type_dump.find(f'{{{URI}}}roundingVAT')
    if rounding_vat_dump is not None:
        rounding_vat = pohoda_mserver_client.schema.type.load_type_rounding_vat(rounding_vat_dump)

    calculate_vat = None
    calculate_vat_dump = invoice_summary_type_dump.find(f'{{{URI}}}calculateVAT')
    if calculate_vat_dump is not None:
        calculate_vat = pohoda_mserver_client.schema.xsd.load_boolean(calculate_vat_dump)

    home_currency = None
    home_currency_dump = invoice_summary_type_dump.find(f'{{{URI}}}homeCurrency')
    if home_currency_dump is not None:
        home_currency = pohoda_mserver_client.schema.type.load_type_currency_home(home_currency_dump)

    foreign_currency = None
    foreign_currency_dump = invoice_summary_type_dump.find(f'{{{URI}}}foreignCurrency')
    if foreign_currency_dump is not None:
        foreign_currency = pohoda_mserver_client.schema.type.load_type_currency_foreign(foreign_currency_dump)

    return InvoiceSummaryType(rounding_document, rounding_vat, calculate_vat, home_currency, foreign_currency)


def load_invoice_type_type(invoice_type_type_dump):
    return pohoda_mserver_client.schema.xsd.load_string(invoice_type_type_dump)


class InvoiceType:

    def __init__(self, header=None, items=None, summary=None):
        self.header = header
        self.items = items
        self.summary = summary

    def __eq__(self, other):
        return (
            self.header == other.header and
            self.items == other.items and
            self.summary == other.summary)


class InvoiceHeaderType:

    def __init__(self, id_=None, type_=None, number=None, sym_var=None, original_document=None, original_document_number=None, sym_par=None, date=None, date_tax=None, date_accounting=None, date_khdph=None, date_due=None, date_application_vat=None, date_delivery=None, accounting=None, classification_vat=None, classification_kvdph=None, number_khdph=None, number_kvdph=None, text=None, partner_identity=None, my_identity=None, price_level=None, payment_type=None, sym_const=None, sym_spec=None, note=None, int_note=None, liquidation=None, mark_record='true'):
        self.id = id_
        self.type = type_
        self.number = number
        self.sym_var = sym_var
        self.original_document = original_document
        self.original_document_number = original_document_number
        self.sym_par = sym_par
        self.date = date
        self.date_tax = date_tax
        self.date_accounting = date_accounting
        self.date_khdph = date_khdph
        self.date_due = date_due
        self.date_application_vat = date_application_vat
        self.date_delivery = date_delivery
        self.accounting = accounting
        self.classification_vat = classification_vat
        self.classification_kvdph = classification_kvdph
        self.number_khdph = number_khdph
        self.number_kvdph = number_kvdph
        self.text = text
        self.partner_identity = partner_identity
        self.my_identity = my_identity
        self.price_level = price_level
        self.payment_type = payment_type
        self.sym_const = sym_const
        self.sym_spec = sym_spec
        self.note = note
        self.int_note = int_note
        self.liquidation = liquidation
        self.mark_record = mark_record

    def __eq__(self, other):
        return (
            self.id == other.id and
            self.type == other.type and
            self.number == other.number and
            self.sym_var == other.sym_var and
            self.original_document == other.original_document and
            self.original_document_number == other.original_document_number and
            self.sym_par == other.sym_par and
            self.date == other.date and
            self.date_tax == other.date_tax and
            self.date_accounting == other.date_accounting and
            self.date_khdph == other.date_khdph and
            self.date_due == other.date_due and
            self.date_application_vat == other.date_application_vat and
            self.date_delivery == other.date_delivery and
            self.accounting == other.accounting and
            self.classification_vat == other.classification_vat and
            self.classification_kvdph == other.classification_kvdph and
            self.number_khdph == other.number_khdph and
            self.number_kvdph == other.number_kvdph and
            self.text == other.text and
            self.partner_identity == other.partner_identity and
            self.my_identity == other.my_identity and
            self.price_level == other.price_level and
            self.payment_type == other.payment_type and
            self.sym_const == other.sym_const and
            self.sym_spec == other.sym_spec and
            self.note == other.note and
            self.int_note == other.int_note and
            self.liquidation == other.liquidation and
            self.mark_record == other.mark_record)


class InvoiceItemType:

    def __init__(self, id_=None, text=None, quantity=None, unit=None, coefficient=1.0, pay_vat='false', rate_vat='none', percent_vat=None, discount_percentage=0.0, home_currency=None, foreign_currency=None, note=None, accounting=None, classification_vat=None, classification_kvdph=None):
        self.id = id_
        self.text = text
        self.quantity = quantity
        self.unit = unit
        self.coefficient = coefficient
        self.pay_vat = pay_vat
        self.rate_vat = rate_vat
        self.percent_vat = percent_vat
        self.discount_percentage = discount_percentage
        self.home_currency = home_currency
        self.foreign_currency = foreign_currency
        self.note = note
        self.accounting = accounting
        self.classification_vat = classification_vat
        self.classification_kvdph = classification_kvdph


class InvoiceSummaryType:

    def __init__(self, rounding_document=None, rounding_vat=None, calculate_vat=None, home_currency=None, foreign_currency=None):
        self.rounding_document = rounding_document
        self.rounding_vat = rounding_vat
        self.calculate_vat = calculate_vat
        self.home_currency = home_currency
        self.foreign_currency = foreign_currency

    def __eq__(self, other):
        return (
            self.rounding_document == other.rounding_document and
            self.rounding_vat == other.rounding_vat and
            self.calculate_vat == other.calculate_vat and
            self.home_currency == other.home_currency and
            self.foreign_currency == other.foreign_currency)

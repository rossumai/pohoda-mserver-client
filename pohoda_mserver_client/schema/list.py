# Copyright (C) 2018 Pohoda-mserver-client authors. See the AUTHORS file found
# in the top-level directory of this distribution.
#
# Licensed under the MIT (Expat) License. See the LICENSE file found in the
# top-level directory of this distribution.

import xml.etree.ElementTree

import pohoda_mserver_client.schema.documentresponse
import pohoda_mserver_client.schema.filter
import pohoda_mserver_client.schema.invoice


URI = 'http://www.stormware.cz/schema/version_2/list.xsd'


def dump_list_invoice_request_type(name, list_invoice_request_type):
    invoice_type_dump = list_invoice_request_type.invoice_type
    request_invoices_dumps = [pohoda_mserver_client.schema.filter.dump_request_invoice_type(f'{{{URI}}}requestInvoice', invoice) for invoice in list_invoice_request_type.request_invoices]

    if len(request_invoices_dumps) < 1:
        raise ValueError()

    list_invoice_request_type_dump = xml.etree.ElementTree.Element(name, {
        'version': '2.0',
        'invoiceType': invoice_type_dump,
        'invoiceVersion': '2.0'})
    list_invoice_request_type_dump.extend(request_invoices_dumps)
    return list_invoice_request_type_dump


def load_list_invoice_type(list_invoice_type_dump):
    version, state = pohoda_mserver_client.schema.documentresponse.load_list_version_type(list_invoice_type_dump)
    if version != '2.0':
        raise ValueError()
    if state == 'error':
        raise ValueError()

    for invoice_dump in list_invoice_type_dump.iterfind(f'{{{URI}}}invoice'):
        yield pohoda_mserver_client.schema.invoice.load_invoice_type(invoice_dump)


class ListInvoiceRequestType:

    def __init__(self, invoice_type, request_invoices):
        self.invoice_type = invoice_type
        self.request_invoices = request_invoices

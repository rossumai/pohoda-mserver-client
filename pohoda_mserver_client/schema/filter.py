# Copyright (C) 2018 Pohoda-mserver-client authors. See the AUTHORS file found
# in the top-level directory of this distribution.
#
# Licensed under the MIT (Expat) License. See the LICENSE file found in the
# top-level directory of this distribution.

import xml.etree.ElementTree

import pohoda_mserver_client.schema.type
import pohoda_mserver_client.schema.xsd


URI = 'http://www.stormware.cz/schema/version_2/filter.xsd'


def dump_filter_docs_type(name, date_from=None, date_till=None, selected_icos=None):
    filter_docs_type_dump = xml.etree.ElementTree.Element(name)
    if date_from is not None:
        filter_docs_type_dump.append(pohoda_mserver_client.schema.xsd.dump_date(f'{{{URI}}}dateFrom', date_from))
    if date_till is not None:
        filter_docs_type_dump.append(pohoda_mserver_client.schema.xsd.dump_date(f'{{{URI}}}dateTill', date_till))
    if selected_icos is not None:
        filter_docs_type_dump.append(dump_selected_ico_type(f'{{{URI}}}selectedIco', selected_icos))
    return filter_docs_type_dump


def dump_group_filter_1(name, date_from=None, date_till=None, selected_icos=None):
    filter_dump = dump_filter_docs_type(f'{{{URI}}}filter', date_from, date_till, selected_icos)

    group_filter_1_dump = xml.etree.ElementTree.Element(name)
    group_filter_1_dump.append(filter_dump)
    return group_filter_1_dump


def dump_request_invoice_type(name, request_invoice_type):
    return dump_group_filter_1(name, request_invoice_type.date_from, request_invoice_type.date_till, request_invoice_type.selected_icos)


def dump_selected_ico_type(name, icos):
    icos_dumps = (pohoda_mserver_client.schema.type.dump_ico_type(f'{{{URI}}}ico', ico) for ico in icos)

    selected_ico = xml.etree.ElementTree.Element(name)
    selected_ico.extend(icos_dumps)
    return selected_ico


class RequestInvoiceType:

    def __init__(self, date_from=None, date_till=None, selected_icos=None):
        self.date_from = date_from
        self.date_till = date_till
        self.selected_icos = selected_icos

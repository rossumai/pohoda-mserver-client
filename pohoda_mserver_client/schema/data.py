# Copyright (C) 2018 Pohoda-mserver-client authors. See the AUTHORS file found
# in the top-level directory of this distribution.
#
# Licensed under the MIT (Expat) License. See the LICENSE file found in the
# top-level directory of this distribution.

import xml.etree.ElementTree

import pohoda_mserver_client.schema.list


URI = 'http://www.stormware.cz/schema/version_2/data.xsd'


def dump_data_pack_type(name, id_, ico, items):
    id_dump = id_
    ico_dump = ico
    items_dumps = [dump_data_pack_item_type(f'{{{URI}}}dataPackItem', item) for item in items]

    if len(items_dumps) < 1:
        raise ValueError()

    data_pack_type_dump = xml.etree.ElementTree.Element(name, {
        'version': '2.0',
        'id': id_dump,
        'ico': ico_dump,
        'application': '',
        'note': ''})
    data_pack_type_dump.extend(items_dumps)
    return data_pack_type_dump


def dump_data_pack_item_type(name, data_pack_item_type):
    id_dump = data_pack_item_type.id
    if isinstance(data_pack_item_type.request, pohoda_mserver_client.schema.list.ListInvoiceRequestType):
        request_dump = pohoda_mserver_client.schema.list.dump_list_invoice_request_type(f'{{{pohoda_mserver_client.schema.list.URI}}}listInvoiceRequest', data_pack_item_type.request)

    data_pack_item_dump = xml.etree.ElementTree.Element(name, {
        'version': '2.0',
        'id': id_dump})
    data_pack_item_dump.append(request_dump)
    return data_pack_item_dump


class DataPackItemType:

    def __init__(self, id_, request):
        self.id = id_
        self.request = request

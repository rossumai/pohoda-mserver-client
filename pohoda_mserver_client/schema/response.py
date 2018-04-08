# Copyright (C) 2018 Pohoda-mserver-client authors. See the AUTHORS file found
# in the top-level directory of this distribution.
#
# Licensed under the MIT (Expat) License. See the LICENSE file found in the
# top-level directory of this distribution.

import pohoda_mserver_client.schema.list


def load_response_pack_type(response_pack_type_dump):
    if response_pack_type_dump.get('version') != '2.0':
        raise ValueError()
    if response_pack_type_dump.get('state') == 'error':
        raise ValueError(response_pack_type_dump.get('note'))

    for item_dump in response_pack_type_dump:
        yield load_response_pack_item_type(item_dump)


def load_response_pack_item_type(response_pack_item_type_dump):
    if response_pack_item_type_dump.get('version') != '2.0':
        raise ValueError()
    if response_pack_item_type_dump.get('state') == 'error':
        raise ValueError(response_pack_item_type_dump.get('note'))

    id_ = response_pack_item_type_dump.get('id')
    if len(response_pack_item_type_dump) == 0:
        response = None
    elif response_pack_item_type_dump[0].tag == f'{{{pohoda_mserver_client.schema.list.URI}}}listInvoice':
        response = pohoda_mserver_client.schema.list.load_list_invoice_type(response_pack_item_type_dump[0])
    else:
        raise ValueError()
    return ResponsePackItemType(id_, response)


class ResponsePackItemType:

    def __init__(self, id_, response):
        self.id = id_
        self.response = response

# Copyright (C) 2018 Pohoda-mserver-client authors. See the AUTHORS file found
# in the top-level directory of this distribution.
#
# Licensed under the MIT (Expat) License. See the LICENSE file found in the
# top-level directory of this distribution.

import urllib.parse
import xml.etree.ElementTree

import requests

import pohoda_mserver_client.schema.data
import pohoda_mserver_client.schema.filter
import pohoda_mserver_client.schema.list
import pohoda_mserver_client.schema.response


def compose_request(baseurl, token, ico, data_pack_id, data_pack_items):
    method = 'POST'
    url = urllib.parse.urljoin(baseurl, '/xml')
    headers = {
            'Content-Type': 'text/xml',
            'STW-Authorization': f'Basic {token}'}
    data_pack_dump = pohoda_mserver_client.schema.data.dump_data_pack_type(f'{{{pohoda_mserver_client.schema.data.URI}}}dataPack', data_pack_id, ico, data_pack_items)
    data = xml.etree.ElementTree.tostring(data_pack_dump, encoding='Windows-1250')
    return requests.Request(method, url, headers, data=data)


def parse_response(response):
    if response.status_code != 200:
        raise ValueError('request failed')

    response_pack_dump = xml.etree.ElementTree.fromstring(response.content)
    return pohoda_mserver_client.schema.response.load_response_pack_type(response_pack_dump)


class Client:

    def __init__(self, session, baseurl, token, ico):
        self.session = session
        self.baseurl = baseurl
        self.token = token
        self.ico = ico

    def request(self, requests_):
        data_pack_items = [pohoda_mserver_client.schema.data.DataPackItemType(str(id_), request) for id_, request in enumerate(requests_)]

        request = compose_request(self.baseurl, self.token, self.ico, '0', data_pack_items)
        response = self.session.send(self.session.prepare_request(request))
        response_pack_items = parse_response(response)

        order = [data_pack_item.id for data_pack_item in data_pack_items]
        response_pack_items = sorted(response_pack_items, key=lambda item: order.index(item.id))
        return (item.response for item in response_pack_items)

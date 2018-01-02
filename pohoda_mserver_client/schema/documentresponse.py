# Copyright (C) 2018 Pohoda-mserver-client authors. See the AUTHORS file found
# in the top-level directory of this distribution.
#
# Licensed under the MIT (Expat) License. See the LICENSE file found in the
# top-level directory of this distribution.

import pohoda_mserver_client.schema.type


URI = 'http://www.stormware.cz/schema/version_2/documentresponse.xsd'


def load_detail_type(detail_type_dump):
    return pohoda_mserver_client.schema.type.load_stav_type(detail_type_dump.find(f'{{{URI}}}state'))


def load_import_details_type(import_details_type_dump):
    for detail_dump in import_details_type_dump:
        yield load_detail_type(detail_dump)


def load_list_version_type(list_version_type_dump):
    version = list_version_type_dump.get('version')
    if version != '2.0':
        raise ValueError()

    state = list_version_type_dump.get('state')
    if state == 'error':
        raise ValueError()

    import_details_dump = list_version_type_dump.find(f'{{{URI}}}importDetails')
    if import_details_dump is not None:
        if 'error' in load_import_details_type(import_details_dump):
            raise ValueError()

    if list_version_type_dump.find(f'{{{URI}}}parts') is not None:
        raise ValueError()

    return version, state

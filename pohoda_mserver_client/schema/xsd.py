# Copyright (C) 2018 Pohoda-mserver-client authors. See the AUTHORS file found
# in the top-level directory of this distribution.
#
# Licensed under the MIT (Expat) License. See the LICENSE file found in the
# top-level directory of this distribution.

import datetime
import xml.etree.ElementTree


def dump_date(name, date):
    date_dump = str(date)

    date_dump_ = xml.etree.ElementTree.Element(name)
    date_dump_.text = date_dump
    return date_dump_


def dump_string(name, string):
    string_dump = str(string)

    string_dump_ = xml.etree.ElementTree.Element(name)
    string_dump_.text = string_dump
    return string_dump_


def load_boolean(boolean_dump):
    return boolean_dump.text == 'true'


def load_date(date_dump):
    datetime_ = datetime.datetime.strptime(date_dump.text, '%Y-%m-%d')
    return datetime_.date()


def load_double(double_dump):
    return float(double_dump.text)


def load_float(float_dump):
    return float(float_dump.text)


def load_integer(integer_dump):
    return int(integer_dump.text)


def load_string(string_dump):
    return string_dump.text

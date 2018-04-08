# Copyright (C) 2018 Pohoda-mserver-client authors. See the AUTHORS file found
# in the top-level directory of this distribution.
#
# Licensed under the MIT (Expat) License. See the LICENSE file found in the
# top-level directory of this distribution.

"""A Sphinx configuration file.

The project version is read from a ``VERSION`` environment variable. If it is
not set, the version is set to "UNKNOWN".

"""

import logging
import os


try:
    version = os.environ['VERSION']
except KeyError:
    logging.warning('"VERSION" environment variable unset')
    version = 'UNKNOWN'

# General configuration
needs_sphinx = '1.5'
extensions = []

# Project information
project = 'Pohoda-mserver-client'
author = 'Pohoda-mserver-client authors'
release = version
copyright = '2018 Pohoda-mserver-client authors'

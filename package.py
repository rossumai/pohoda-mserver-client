#!/usr/bin/env python
#
# Copyright (C) 2018 Pohoda-mserver-client authors. See the AUTHORS file found
# in the top-level directory of this distribution.
#
# Licensed under the MIT (Expat) License. See the LICENSE file found in the
# top-level directory of this distribution.

"""A script that performs various packaging tasks.

The usage is::

    package.py [-h] [--destination DESTINATION] version download_url

"""

import argparse
import base64
import csv
import hashlib
import importlib.machinery
import pathlib
import shutil
import tempfile
import zipfile


NAME = 'pohoda-mserver-client'
SUMMARY = 'A library that provides a Python API to POHODA mServers.'
DESCRIPTION = 'It is a library that solves a problem of how to interact with POHODA mServers programmatically, by providing means to send various requests and parse the following responses.'
KEYWORDS = {'POHODA', 'mServer', 'API', 'client'}
HOMEPAGE = 'https://github.com/rossumai/pohoda-mserver-client'
AUTHOR = 'Pohoda-mserver-client authors'
STATUS_CLASS = '4 - Beta'
AUDIENCE_CLASSES = {'Developers'}
LICENSE_CLASS = 'OSI Approved :: MIT License'
NATURAL_LANGUAGE_CLASSES = {'English'}
TOPIC_CLASSES = {'Software Development :: Libraries :: Python Modules'}
REQUIRED_DISTS = {'requests (>=2.18,<3)'}
PROJECT_URLS = {'issue tracking system, https://github.com/rossumai/pohoda-mserver-client/issues'}
PACKAGE = 'pohoda_mserver_client'

SYSTEM_CLASS = 'OS Independent'
PLATFORM_TAG = 'any'

PROGRAMMING_LANGUAGE_CLASSES = {'Programming Language :: Python :: 3.6'}
REQUIRED_PYTHON = '>=3.6,<4'
PYTHON_TAG = 'py36'
PYTHON_ABI_TAG = 'none'


def create_wheel(version, download_url, destination):
    with tempfile.TemporaryDirectory() as workdir_name:
        workdir = pathlib.Path(workdir_name)

        distinfo = workdir / f'{NAME}-{version}.dist-info'
        distinfo.mkdir()

        with distinfo.joinpath('WHEEL').open('w', encoding='utf-8') as distinfo_wheel_file:
            distinfo_wheel_file.write(
                f'Wheel-Version: 1.0\n'
                f'Generator: {NAME} {version}\n'
                f'Root-Is-Purelib: true\n'
                f'Tag: {PYTHON_TAG}-{PYTHON_ABI_TAG}-{PLATFORM_TAG}')

        with distinfo.joinpath('METADATA').open('w', encoding='utf-8') as distinfo_metadata_file:
            distinfo_metadata_file.write(
                f'Metadata-Version: 1.2\n'
                f'Name: {NAME}\n'
                f'Version: {version}\n'
                f'Summary: {SUMMARY}\n'
                f'Description: {DESCRIPTION}\n'
                f'Keywords: {" ".join(KEYWORDS)}\n'
                f'Home-page: {HOMEPAGE}\n'
                f'Download-URL: {download_url}\n'
                f'Author: {AUTHOR}\n'
                f'Classifier: Development Status :: {STATUS_CLASS}\n'
                f'Classifier: License :: {LICENSE_CLASS}\n'
                f'Classifier: Operating System :: {SYSTEM_CLASS}\n'
                f'Provides-Dist: {NAME} {version}\n'
                f'Requires-Python: {REQUIRED_PYTHON}\n')
            for audience_class in AUDIENCE_CLASSES:
                distinfo_metadata_file.write(f'Classifier: Intended Audience :: {audience_class}\n')
            for natural_language_class in NATURAL_LANGUAGE_CLASSES:
                distinfo_metadata_file.write(f'Classifier: Natural Language :: {natural_language_class}\n')
            for programming_language_class in PROGRAMMING_LANGUAGE_CLASSES:
                distinfo_metadata_file.write(f'Classifier: Programming Language :: {programming_language_class}\n')
            for topic_class in TOPIC_CLASSES:
                distinfo_metadata_file.write(f'Classifier: Topic :: {topic_class}\n')
            for required_dist in REQUIRED_DISTS:
                distinfo_metadata_file.write(f'Requires-Dist: {required_dist}\n')
            for project_url in PROJECT_URLS:
                distinfo_metadata_file.write(f'Project-URL: {project_url}\n')

        bytecode_patterns = ('*' + ext for ext in importlib.machinery.BYTECODE_SUFFIXES)
        shutil.copytree(PACKAGE, str(workdir / PACKAGE), ignore=shutil.ignore_patterns(*bytecode_patterns))

        distinfo_record = distinfo.joinpath('RECORD')
        with distinfo_record.open('w', encoding='utf-8', newline='') as distinfo_record_file:
            writer = csv.writer(distinfo_record_file, delimiter=',', quotechar='"', lineterminator='\n')
            for workfile in walk_files(workdir):
                writer.writerow((
                    '/'.join(workfile.relative_to(workdir).parts),
                    '' if workfile == distinfo_record else 'sha256=%s' % hash_file(workfile),
                    '' if workfile == distinfo_record else str(workfile.stat().st_size)))

        with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as wheel_file:
            for workfile in walk_files(workdir):
                wheel_file.write(str(workfile), str(workfile.relative_to(workdir)))


def walk_files(directory):
    for child in directory.iterdir():
        if child.is_dir():
            yield from walk_files(child)
        else:
            yield child


def hash_file(path):
    hash_ = hashlib.sha256()
    with path.open('rb') as file:
        while True:
            chunk = file.read(16 * 1024)
            if not chunk:
                break
            hash_.update(chunk)
    return base64.urlsafe_b64encode(hash_.digest()).rstrip(b'=').decode('ascii')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--destination')
    parser.add_argument('version')
    parser.add_argument('download_url')
    arguments = parser.parse_args()

    destination = arguments.destination
    if destination is None:
        destination = f'{NAME}-{arguments.version}-{PYTHON_TAG}-{PYTHON_ABI_TAG}-{PLATFORM_TAG}.whl'

    create_wheel(arguments.version, arguments.download_url, destination)

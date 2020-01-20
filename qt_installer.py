#! /usr/bin/env python3
import argparse
import os
import re
import xml.etree.ElementTree as ElementTree

import requests

REPO_URL = 'https://download.qt.io/online/qtsdkrepository/linux_x64/desktop'
ARCH = 'gcc_64'


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--version', type=str,
                        help='Qt version <Required>', required=True)
    parser.add_argument('-m', '--modules', action='append',
                        default=[ARCH], help='Modules to install')

    parser.set_defaults(func=install)
    return parser.parse_args()


def install(params):
    version = params.version
    qt_version = ''.join(re.findall(r'\d', version))
    packages = get_packages(qt_version, params.modules)
    for pkg in packages:
        print('    Install package:\033[1m', pkg['name'], '\033[0m\033[K')
        for url in pkg['archives']:
            archive = re.sub(r'-Linux.+', '', url.split('/')[-1])
            print('\033[KDownloading {} \033[A'.format(archive))
            os.system('wget -q -O package.7z ' + url)

            print('\033[KExtracting {} \033[A'.format(archive))
            os.system('7z x package.7z 1>/dev/null')
            os.system('rm package.7z')

        print('\033[A\033[1;32mOK\033[0m')
    os.system('echo -n "[Paths]\nPrefix = .." > $PWD/{0}/gcc_64/bin/qt.conf'.format(version))
    os.system('echo -n "[Paths]\nPrefix = .." > $PWD/{0}/gcc_64/libexec/qt.conf'.format(version))
    fix_license(version)
    print('\033[KInstallation Finished.')


def get_packages(qt_version, modules):
    xml_url = '/'.join([REPO_URL, 'qt5_' + qt_version, 'Updates.xml'])
    xml_resp = requests.get(xml_url)
    xml = ElementTree.fromstring(xml_resp.content)

    packages = []
    for package in xml.findall('PackageUpdate'):
        name = package.find('Name').text
        module = re.sub(
            r'.+?\.{}\.(.+?)(?:\.{}|$)'.format(qt_version, ARCH), r'\1', name)
        if name.endswith(ARCH) and module in modules:
            pkg_version = package.find('Version').text
            archives = package.find('DownloadableArchives').text.split(', ')

            archives = ['/'.join([REPO_URL, 'qt5_' + qt_version, name,
                             pkg_version + archive]) for archive in archives]
            packages.append({'name': name, 'archives': archives})
    return packages


def fix_license(version):
    lic_file = './{}/gcc_64/mkspecs/qconfig.pri'.format(version)
    _lic = open(lic_file, 'r').read()
    with open(lic_file, 'w') as file:
        _lic = re.sub(r'(QT_EDITION\s=\s)Enterprise', r'\1OpenSource', _lic, re.I)
        _lic = re.sub(r'(QT_LICHECK\s=\s)\S+', r'\1', _lic, re.I)
        file.write(_lic)
        file.close()


if __name__ == '__main__':
    args = parse_args()
    args.func(args)

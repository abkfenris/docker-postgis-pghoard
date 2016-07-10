#!/usr/bin/env python
import os
import shutil
import subprocess

postgres_versions = ['9.1', '9.2', '9.3', '9.4', '9.5']
postgis_versions = ['2.2']
pghoard_versions = ['1.2.0', '1.3.0']

build_files = ['README.md', 'initdb-pghoard.sh', 'docker-entrypoint.sh']

versions = [(pg, gis, ph) for pg in postgres_versions
            for gis in postgis_versions
            for ph in pghoard_versions]

with open('Dockerfile.template') as f:
    template = f.read()

current_path = os.path.dirname(os.path.abspath(__file__))

try:
    build = str(raw_input('docker build files? [y/N]')).lower() == 'y'
except SyntaxError:
    build = False

for version in versions:
    pg, gis, ph = version

    folder = '{pg}-{gis}-{ph}'.format(pg=pg, gis=gis, ph=ph)
    path = os.path.join(current_path, folder)

    print('Updating {folder}'.format(folder=folder))

    try:
        os.mkdir(path)
    except OSError:
        pass
    dockerfile = template.format(pg_version=pg, pghoard_version=ph)

    dfile = os.path.join(path, 'Dockerfile')
    with open(dfile, 'w') as f:
        f.write(dockerfile)

    for f_name in build_files:
        shutil.copyfile(os.path.join(current_path, f_name),
                        os.path.join(path, f_name))

    if build:

        subprocess.call(['docker', 'build', '-t', 'abkfenris/postgis-pghoard:' + pg + '-' + ph, path])

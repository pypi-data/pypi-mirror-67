#!/usr/bin/env python
import os
import shutil
from codecs import open
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import call

here = os.path.abspath(os.path.dirname(__file__))
pkg_name = 'zwnlp'
packages = [pkg_name]

install_in_custom = ['torch', 'torchvision']
test_requirements = [s.strip() for s in open('requirements_dev.txt').readlines()][4:]
requires = [s.strip() for s in open('requirements.txt').readlines()]
requires_custom = []
_requires = []
_wheellink = ''
for r in requires:
    if r.startswith('-f'):
        _wheellink = r
    else:
        is_cust = False
        for c in install_in_custom:
            if r.startswith(c):
                r = r.split('#')[0].strip()
                is_cust = True
                break
        if is_cust:
            requires_custom.append(r)
        else:
            _requires.append(r)
requires = _requires

class CustomInstall(install):
    def run(self):
        for c in requires_custom:
            call(['pip', 'install', c, '-f %s'%_wheellink])
        install.run(self)

shutil.rmtree('dist', ignore_errors=True)
about = {}
lines = []
with open(os.path.join(here, pkg_name, '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)
    # auto update min version number for every dist upload
    verarr = about['__version__'].split('.')
    verarr[2] = str(int(verarr[2])+1)
    about['__version__'] = '.'.join(verarr)
    f.seek(0)
    lines = f.readlines()
    lines[0] = "__version__ = '%s'\n"%about['__version__']
with open(os.path.join(here, pkg_name, '__version__.py'), 'w', 'utf-8') as f:
    f.writelines(lines)

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    cmdclass={
        'install': CustomInstall,
    },
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={pkg_name:pkg_name},
    include_package_data=True,
    install_requires=requires,
    tests_require=test_requirements,
    python_requires='>=3.6',
    platforms=["all"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
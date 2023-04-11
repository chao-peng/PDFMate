# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='PDFMate',
    version='0.1.0',
    description='Simple PDF merge and split tool',
    long_description=readme,
    author='Chao Peng',
    author_email='chao.peng@acm.org',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={"console_scripts": ["pdfmate = pdfmate.__main__:main"]},
    scripts=["pdfmate/__main__.py"]
)

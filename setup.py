import os
from setuptools import setup


setup(
    name="ascii_binder_search",
    version="0.0.1",
    author="smit thakkar",
    author_email="smitthakkar96@gmail.com",
    description=("A small utility that would help you to get search in asciibinder"),
    package_data={'static': '*'},
    license="BSD",
    keywords="Asciibinder, ascii_binder_search",
    url="https://github.com/smitthakkar96/ascii_binder_search_plugin",
    install_requires=['lxml', 'pyyaml', 'xmltodict', 'beautifulsoup4', 'xmltodict'],
    py_modules=['ascii_binder_search'],
    data_files=['static/search.html'],
    include_package_data=True,
    zip_safe=False,
    scripts=[
        'ascii_binder_search'
    ]
)

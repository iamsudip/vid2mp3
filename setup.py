#!/usr/bin/env python

'''
Commandline tool to download youtube flash videos as mp3.
It communicates with listentoyoutube.com for this purpose.
Vimeo.com, dailymotion.com, metacafe.com are also supported by this tool.
'''

requirements = []

with open('README') as text:
    long_description = text.read()

try:
    from setuptools import setup, find_packages
except ImportError:
    requirements.append('setuptools')
try:
    import BeautifulSoup
except ImportError:
    requirements.append('BeautifulSoup4')
try:
    import lxml
except ImportError:
    requirements.append('lxml')
try:
    import requests
except ImportError:
    requirements.append('requests')

setup(name = 'vid2mp3',
    version = '0.1.3',
    description = "Script to extract audio only from online videos",
    long_description = long_description,
    platforms = ["Linux"],
    author = "iamsudip",
    author_email = "iamsudip@programmer.net",
    url = "https://github.com/iamsudip/vid2mp3",
    license = "MIT",
    packages = find_packages(),
    install_requires = requirements,
    dependency_links = ['https://pypi.python.org/pypi/requests/1.2.3',
                        'https://pypi.python.org/pypi/beautifulsoup4/4.3.2',
                        'https://pypi.python.org/pypi/setuptools/0.6c11',
                        'https://pypi.python.org/pypi/lxml/2.3.2'
],
    include_package_data = True,
    scripts = ['vid2mp3'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Video',
        'Topic :: Utilities',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
]
    )

#from distutils.core import setup
from setuptools import setup
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name = 'AESClient',
    packages = ['AESClient'],
    version = '0.0.0.0.2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author = 'Shaon Majumder',
    author_email = 'smazoomder@gmail.com',
    url = 'https://github.com/ShaonMajumder/AESClient',
    download_url = 'https://github.com/ShaonMajumder/AESClient/archive/0.0.0.0.2.tar.gz',
    keywords = ['AES', 'Encryption', 'Security', 'Shaon', 'Majummder'],
    classifiers = [],
    setup_requires=['wheel']
)
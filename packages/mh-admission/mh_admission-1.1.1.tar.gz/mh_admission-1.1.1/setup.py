"""Setup for packaging Tool for parsing and creating a structured data out of PDF to excel to MySql tables"""

__author__ = "Prasad S. Deshpande."
__copyright__ = "Copyright 2020"

import os
from setuptools import setup, find_packages
import re
from os import path


def read(fname):
    '''Utility function to read the contents of a file.'''
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def load_version():
    """ Loads a file content """
    filename = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                            "maha_cet_parser", "__init__.py"))
    with open(filename, "rt") as version_file:
        mh_cet_admission_init = version_file.read()
        version = re.search(r"__version__ = '([0-9a-z.-]+)'", mh_cet_admission_init).group(1)
        return version


def generate_long_description_file():
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(name='mh_admission',
      version=load_version(),
      description='Maharashtra admission tools',
      url='https://gitlab.com/prasad.deshpande13/mh_cet_admission_utils',
      author='Deshpande Prasad S.',
      author_email='prasad.deshpande13@gmail.com',
      packages=find_packages(),
      entry_points={'console_scripts': ['mh_admission=maha_cet_parser:maha_cet_parser_tools_cli']},
      zip_safe=False,
      include_package_data=True,
      install_requires=['SQLAlchemy~=1.3.1', 'ConfigArgParse~=1.0', 'xlrd~=1.2.0', 'setuptools~=46.1.3', 'pymysql'],
      package_data={
          # If any package contains *.txt or *.ps1 files, include them:
          '': ['*.pdf', "*.xlsx"]

      },
      long_description=generate_long_description_file(),
      long_description_content_type='text/markdown'
      )

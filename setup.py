#!/usr/bin/env python
from setuptools import setup

setup(name='options',
      version='0.0.1',
      description='Options for django admin. Administrator emails, phones, contact data, etc.',
      long_description='',
      author='Vital Belikov',
      author_email='vital@qwe.lv',
      packages=['options', 'options.migrations', 'options.templatetags'],
      url='https://github.com/Brick85/options/',
      include_package_data = True,
      zip_safe = False,
      requires=['django(>=1.3)'],
      classifiers=['Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License'],
      license='New BSD')

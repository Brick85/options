#!/usr/bin/env python
from setuptools import setup

setup(name='django-qoptions',
      version='0.0.2',
      description='Options for django admin. Emails, phones, contact data, etc.',
      long_description='Options package allows you to create record in database, wich you can use in your templates and views.',
      author='Vital Belikov',
      author_email='vital@qwe.lv',
      packages=['options', 'options.migrations', 'options.templatetags'],
      url='https://github.com/Brick85/options/',
      include_package_data = True,
      zip_safe = False,
      requires=['django(>=1.3)'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Operating System :: Unix',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Utilities'],
      license='New BSD')

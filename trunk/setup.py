#!/usr/bin/env python

from distutils.core import setup

setup(name='cl-calc',
      version='0.1.1',
      description='A simple calculator',
      author='Sean Gillespie',
      author_email='Sean.Gillespie@bisonofborg.com',
      url='http://www.bisonofborg.com',
      packages=['interpreter', 'objects', 'lib'],
      scripts=['cl-calc.py'],
    )

#!/usr/bin/env python

from os import path

from setuptools import setup
from setuptools import find_packages


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(name='genre',
      version='0.1.1',
      description='a concise and simple requirements.txt generator',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Baichuan Li',
      author_email='baichuan@outlook.com',
      url='https://github.com/BaichuanLi/genre',
      license='MIT',
      install_requires=[
          'setuptools'
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
          'Operating System :: OS Independent'
      ],
      entry_points={
          'console_scripts': ['genre=genre.genre:main'],
      },
      packages=find_packages())

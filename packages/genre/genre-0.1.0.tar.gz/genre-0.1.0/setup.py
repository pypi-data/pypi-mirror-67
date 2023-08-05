#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages


setup(name='genre',
      version='0.1.0',
      description='a concise and simple requirements.txt generator',
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

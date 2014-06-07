#!/usr/bin/env python
from setuptools import setup

setup(name="twitter_interface",
      version="0.01",
      author="Raymond Klass",
      author_email="raymond.klass@gmail.com",
      description="Twitter Extractor",
      license="MIT",
      packages=["twitter_interface"],
      install_requires=['tweepy', ],
      url="https://github.com/RaymondKlass/twitter-extractor",
      )
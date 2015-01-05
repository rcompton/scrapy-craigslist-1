from setuptools import setup

config = {
    'name': 'scrapy-craigslist',
    'description': 'A configurable crawler for craigslist',
    'author': 'Curtis Mattoon',
    'author_email': 'cmattoon@cmattoon.com',
    'install_requires': ['scrapy', 'beautifulsoup4']
}

setup(**config)

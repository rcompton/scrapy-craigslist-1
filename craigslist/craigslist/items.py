# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CraigslistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Posting(scrapy.Item):
    """Intuitively, the URL to the post.
    """
    postUrl = scrapy.Field()

    """This is the city/region of the post
    """
    subdomain = scrapy.Field()

    """The posting title
    """
    title = scrapy.Field()

    """The date the post was posted
    """
    postDate = scrapy.Field()

    """The content of the post
    """
    body = scrapy.Field()

    """URLs for any images
    """
    images = scrapy.Field()
    

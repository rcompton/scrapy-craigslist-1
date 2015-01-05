import scrapy
import scllib

class CraigslistSpider(scrapy.Spider):
    name = 'CraigslistSpider'
    start_urls = scllib.get_start_url()

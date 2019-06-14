# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    goodsid = scrapy.Field()
    title = scrapy.Field()
    shop = scrapy.Field()
    goodslink = scrapy.Field()
    shoplink = scrapy.Field()
    price = scrapy.Field()
    goodrate = scrapy.Field()

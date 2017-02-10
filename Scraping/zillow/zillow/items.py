# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZillowItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    post_name = scrapy.Field()
    price = scrapy.Field()
    bedrooms = scrapy.Field()
    address = scrapy.Field()
    lat = scrapy.Field()
    lon = scrapy.Field()
    featurs = scrapy.Field()
    
    pass

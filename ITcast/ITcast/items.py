# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 与itcast.py 定义的一一对应
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()


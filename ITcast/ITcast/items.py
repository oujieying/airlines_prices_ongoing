# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ItcastItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 与itcast.py 定义的一一对应
    name = Field()
    title = Field()
    info = Field()


class MinPriceItem(Item):
    depcity = Field()
    depcityname_en = Field()
    depcityname_zh = Field()
    region = Field()
    region_code = Field()

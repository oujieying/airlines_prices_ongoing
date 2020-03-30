# -*- coding: utf-8 -*-

import sys

sys.path.append('../')
from scrapy import Request, Spider, cmdline
import re
import json

# 导入容器


# from items import ItcastItem
from items import MinPriceItem


class ItcastSpider(Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']

    # 起始url列表  爬虫的第一批请求，将求这个列表里获取
    #  start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    min_price_url = "https://b2c.csair.com/portal/minPrice/queryMinPriceInAirLines?jsoncallback=getMinPrice&inter=N" \
                    "&callback=getMinPrice&_=1585548643336"

    def start_requests(self):
        yield Request(self.min_price_url, callback=self.parse_min_price)

    def parse_min_price(self, response):
        pattern = r'getMinPrice\((.*)\)'
        result = re.match(pattern, response.text)
        from_flights = json.loads(result.group(1)).get('FROMOFLIGHTS')
        # self.logger.debug(from_flights)
        for item in from_flights:
            min_price_item = MinPriceItem()
            min_price_item['depcity'] = item.get('DEPCITY')
            min_price_item['depcityname_en'] = item.get('DEPCTIYNAME_EN')
            min_price_item['depcityname_zh'] = item.get('DEPCTIYNAME_ZH')
            min_price_item['region'] = item.get('REGION')
            min_price_item['region_code'] = item.get('REGION_CODE')
            flights = []
            for flight_item in item.get('FLIGHT'):
                flight = {"depdate": flight_item.get('DEPDATE'), 'money': flight_item.get('money'),
                          'arrcityname_en': flight_item.get('ARRCITYNAME_EN'), 'arrcity': flight_item.get('ARRCITY'),
                          'returndate': flight_item.get('RETURNDATE'), 'segtype': flight_item.get('SEGTYPE'),
                          'arrcityname_zh': flight_item.get('ARRCTIYNAME_ZH'), 'minprice': flight_item.get('MINPRICE')}
                flights.append(flight)
            min_price_item['flight'] = flights
            yield min_price_item


# def parse(self, response):
# node_list = response.xpath("//div[@class='li_txt']")
# for node in node_list:
#     # 创建item字段对象，用来存储信息
#     item = ItcastItem()
#
#     # .extract() 将xpath对象转换为Unicode字符串
#     name = node.xpath("./h3/text()").extract()
#     title = node.xpath("./h4/text()").extract()
#     info = node.xpath("./p/text()").extract()
#
#     item['name'] = name[0]
#     item['title'] = title[0]
#     item['info'] = info[0]
#     # 返回提取到的每一个item数据 给管道文件处理，同时还会回来继续执行后面的代码
#     yield item

if __name__ == '__main__':
    cmdline.execute("scrapy crawl itcast".split())

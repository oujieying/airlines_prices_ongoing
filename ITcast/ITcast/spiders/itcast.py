# -*- coding: utf-8 -*-
import scrapy


#导入容器

from ITcast.items import ItcastItem
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']

    # 起始url列表  爬虫的第一批请求，将求这个列表里获取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")
        for node in node_list:
            # 创建item字段对象，用来存储信息
            item = ItcastItem()

            # .extract() 将xpath对象转换为Unicode字符串
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            # 返回提取到的每一个item数据 给管道文件处理，同时还会回来继续执行后面的代码
            yield item


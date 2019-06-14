# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from duanzi.items import DuanziItem
from scrapy_redis.spiders import RedisCrawlSpider


class QiushiSpider(RedisCrawlSpider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['https://www.qiushibaike.com/text/']
    redis_key = 'qiushi:start_urls'
    rules = (
        Rule(LinkExtractor(allow=r'/article/\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/text/page/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = DuanziItem()
        i['name'] = response.xpath("//span[@class='side-user-name']/text()").extract()
        i['content'] = response.xpath("//div[@class='content']/text()").extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        yield i

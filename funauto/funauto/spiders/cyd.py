# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from funauto.items import FunautoItem


class CydSpider(CrawlSpider):
    name = 'cyd'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['http://qiushibaike.com/text/']

    def start_requests(self):
        ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        yield Request('http://qiushibaike.com/',headers=ua)
    rules = (
        Rule(LinkExtractor(allow=r'article'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = FunautoItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['content'] = response.xpath("//div[@class='content']/text()").extract()
        i['link'] = response.xpath("//link[@rel='canonical']/@href").extract()
        yield i

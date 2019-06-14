# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request


class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://dangdang.com/']

    def parse(self, response):
        item = DangdangItem()
        item['title'] = response.xpath('//a[@name="itemlist-picture"]/@title').extract()
        item['link'] = response.xpath('//a[@name="itemlist-picture"]/@href').extract()
        item['comment'] = response.xpath('//a[@class="search_comment_num"]/text()').extract()
        yield item
        for i in range(1, 100):
            url = 'http://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA&act=input&page_index=' + str(i)
            yield Request(url, callback=self.parse)
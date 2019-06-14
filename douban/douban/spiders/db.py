# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest


class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']

    ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    #start_urls = ['http://douban.com/']
    def start_requests(self):
        yield Request('https://accounts.douban.com/j/mobile/login/basic',headers=self.ua, callback=self.parse, meta={'cookiejar':1})
    def parse(self, response):
        url = 'https://accounts.douban.com/j/mobile/login/basic'
        print('no yanzhengma')
        data = {"username": '17326063568',
                "password": 'cyd1994920', }
        print('loging')
        return [FormRequest.from_response(response, meta={'cookiejar':response.meta['cookiejar']},
                                          headers=self.ua,
                                          formdata=data,
                                          callback=self.next,
                                          )]
    def next(self):
        print('success')


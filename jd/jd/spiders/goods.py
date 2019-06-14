# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jd.items import JdItem
import re
import urllib.request

class GoodsSpider(CrawlSpider):
    name = 'goods'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        try:
            i = JdItem()
            thisurl = response.url
            pat = 'item.jd.com.*?(\d+).html'
            x = re.search(pat, thisurl)
            if x:
                thisid = re.compile(pat).findall(thisurl)[0]
                print(thisid)
                title = response.xpath('//html/head/title/text()').extract()
                shop = response.xpath('//div[@class="name"]/a/text()').extract()
                shoplink = response.xpath('//div[@class="name"]/a/@href').extract()
                priceurl = 'https://p.3.cn/prices/mgets?callback=jQuery8766554&type=1&area=1_72_4137_0&pdtk=&pduid=15048784180911725795195&pdpin=&pin=null&pdbp=0&skuIds=J_' + str(thisid)
                commenturl = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv10&productId=' + str(thisid) + '&score=0&sortType=5&page=3&pageSize=10&isShadowSku=100001918171&rid=0&fold=1'
                #print(priceurl)
                #print(commenturl)
                pricedata = urllib.request.urlopen(priceurl).read().decode('utf-8', 'ignore')
                commentdata = urllib.request.urlopen(commenturl).read().decode('utf-8', 'ignore')
                pricepat = '"p":"(.*?)"'
                commentpat = '"goodRateShow":(.*?),'
                price = re.compile(pricepat).findall(pricedata)
                comment = re.compile(commentpat).findall(commentdata)
                if (len(title)) and (len(shop)) and (len(shoplink)) and (len(price)) and (len(comment)):
                    i['goodsid'] = thisid
                    i['title'] = title[0]
                    i['shop'] = shop[0]
                    i['goodslink'] = thisurl
                    i['shoplink'] = 'https:' + shoplink[0]
                    i['price'] = price[0]
                    i['goodrate'] = comment[0]
                    print(title[0])
                    print(thisurl)
                    print(shop[0])
                    print('https:' + shoplink[0])
                    print(price[0])
                    print(comment[0])
                    print('-----------')
                else:
                    pass
            else:
                pass
            yield i
        except Exception as e:
            print(e)

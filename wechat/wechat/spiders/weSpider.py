#coding=utf-8
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from wechat.items import WechatItem

class weSpider(scrapy.spiders.Spider):
    name = "weSpider"
    start_urls = ["http://mp.weixin.qq.com/s?timestamp=1463127018&src=3&ver=1&signature=mNPkSOqWJD-E-l8UBwRa3IiBjKbc8SW2tfDhHxlQGfJRVLRbmocGVQAX2gBvjSLlXtQQPxcpzWwhjIB5paKAQxLS3sYKXhYdklLK*8mV5tCmt00JiLMJZaXmCB6yiXayRsu3OqIxY6NFV12c9Y-kEDirOWkG0XXjZTFg8*R1MEQ="]
    def parse(self,response):
        sel =Selector(response)
        item = WechatItem()
        a = sel.xpath("//title")
        a = a.xpath("text()").extract()
        a = str(a)
        print a
        f = open('native.txt','w')
        f.write(a)
        f.close()
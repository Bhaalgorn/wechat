#coding=gbk
import scrapy
import re
from scrapy.selector import Selector
from scrapy.http import Request
from wechat.items import WechatItem

class weSpider(scrapy.spiders.Spider):
    name = "weSpider"
    start_urls = ["http://mp.weixin.qq.com/s?timestamp=1463127018&src=3&ver=1&signature=mNPkSOqWJD-E-l8UBwRa3IiBjKbc8SW2tfDhHxlQGfJRVLRbmocGVQAX2gBvjSLlXtQQPxcpzWwhjIB5paKAQxLS3sYKXhYdklLK*8mV5tCmt00JiLMJZaXmCB6yiXayRsu3OqIxY6NFV12c9Y-kEDirOWkG0XXjZTFg8*R1MEQ="]
    def parse(self,response):
        sel =Selector(response)
        item = WechatItem()
        a = sel.xpath('//h2[@class="rich_media_title"][1]')
        item['title'] = a.xpath("text()").extract()
        yield item
        #a = str(a)
        #m = re.match('^\[u\'(.*?)\'\]$',a)
        #print '你好'
        #s = m.group(1)
        #print s
        #s = s.encode('utf-8')
        #print s
        #f = open('native1.txt','w')
        #f.write(a)
        #f.close()
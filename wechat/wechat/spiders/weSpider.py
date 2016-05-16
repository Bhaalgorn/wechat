import scrapy
from scrapy.selector import Selector

class weSpider(scrapy.spiders.Spider):
    name = "weSpider"
    start_url = ["http://mp.weixin.qq.com/s?timestamp=1463127018&src=3&ver=1&signature=mNPkSOqWJD-E-l8UBwRa3IiBjKbc8SW2tfDhHxlQGfJRVLRbmocGVQAX2gBvjSLlXtQQPxcpzWwhjIB5paKAQxLS3sYKXhYdklLK*8mV5tCmt00JiLMJZaXmCB6yiXayRsu3OqIxY6NFV12c9Y-kEDirOWkG0XXjZTFg8*R1MEQ="]
    def parse(self,response):
        filename = 'excited'
        with open(filename,'wb') as f:
            f.write(response.body)
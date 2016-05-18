# -*- coding: utf-8 -*-
import re
from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
import MySQLdb
import MySQLdb.cursors
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WechatPipeline(object):
    def __init__(self):

        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            host = '127.0.0.1',
            db = 'testwechat',
            user = 'root',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
        )
    def process_item(self, item, spider):
        print spider
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)

        return item
    def _conditional_insert(self, tx, item):
            tx.execute("insert into result (we_title,we_body)values (%s,%s)",(item['title'][0],item['body'][0]))

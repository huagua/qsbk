# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("jianjie.json", "w", encoding='utf-8')

    @staticmethod
    def open_spider(self):
        print("爬虫开始啦。。。。。")

    def process_item(self, item, spider):
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.fp.write(item_json+'\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
        print("爬虫结束了。。。。。")

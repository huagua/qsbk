# -*- coding: utf-8 -*-
import pprint

import scrapy
from qsbk.items import QsbkItem


class WeixinSpider(scrapy.Spider):
    name = 'weixin'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=1&page=1']

    def parse(self, response):
        tiezis = response.xpath('//div[@class="mbox_list recommend_article_list cl"]')
        for tiezi in tiezis:
            detail_url = tiezi.xpath('./a/@href').get()
            title = tiezi.xpath('.//h3//text()').get()
            content = tiezi.xpath('.//div[@class="recommend_article_list_simple"]//text()').get()
            time = tiezi.xpath('.//div[@class="recommend_article_list_info"]/text()').getall()
            item = QsbkItem(detail_url=detail_url, title=title, content=content, time=time)
            yield item


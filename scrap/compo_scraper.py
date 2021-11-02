# -*- coding: utf-8 -*-
import scrapy


class BlogSpider(scrapy.Spider):
    name = 'compospider'
    start_urls = [
        'https://www.hearthstonetopdecks.com/guides/hearthstone-battlegrounds-heroes-tier-list-guides/#t1']

    def parse(self, response):
        for link in response.css('div.entry-content ul li'):
            if link is not None:
                yield {'character': link.css('a ::text').extract_first()}

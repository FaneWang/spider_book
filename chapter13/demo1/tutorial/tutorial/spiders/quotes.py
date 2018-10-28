# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from ..items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item

        next_page = response.css('.page .next a::attr("href")').extract_first()
        url = response.urljoin(next_page)
        yield scrapy.Request(url=url, callback=self.parse)

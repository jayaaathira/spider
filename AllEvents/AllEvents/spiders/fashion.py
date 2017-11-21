# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from AllEvents.items import AlleventsItem

class FashionSpider(scrapy.Spider):
    name = 'fashion'
    allowed_domains = ['www.olx.in']
    start_urls = ['https://www.olx.in/men/',
		  'https://www.olx.in/women/',
	          'https://www.olx.in/kids/'
    ]
    rules = (
		Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
		   callback="parse_item",
		   follow=True),)
    def parse(self, response):
	item_links = response.css('.large > .detailsLink::attr(href)').extract()
 	for a in item_links:
           yield scrapy.Request(a, callback=self.parse_detail_page)
    def parse_detail_page(self, response):
        title = response.css('h1::text').extract()[0].strip()
	price = response.css('.pricelabel > strong::text').extract()[0]
	item =AlleventsItem()
	item['title'] = title
	item['price'] = price
	item['url'] = response.url
	yield item

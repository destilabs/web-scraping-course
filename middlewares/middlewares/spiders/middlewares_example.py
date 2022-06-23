import scrapy


class MiddlewaresExampleSpider(scrapy.Spider):
    name = 'middlewares_example'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        pass

import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    #allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')

        for quote in quotes:
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract_first()

            yield {
                'text': text,
                'author': author,
                'tags': tags
            }

            next_page = response.css('li.next a::attr(href)').get()

            if next_page:
                yield scrapy.Request(response.urljoin(next_page))
            

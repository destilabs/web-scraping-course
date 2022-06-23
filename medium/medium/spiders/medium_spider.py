import scrapy
from datetime import date, timedelta

def daterange(startdate, end_date):
    for n in range(int((end_date - startdate).days)):
        yield startdate + timedelta(n)

class MediumSpiderSpider(scrapy.Spider):
    name = 'medium_spider'

    start_date = date(2021, 1, 1)
    end_date = date(2021, 2, 1)

    date_str = end_date.strftime("/%Y/%m/%d")

    def start_requests(self):
        for single_data in daterange(self.start_date, self.end_date):
            date_str = single_data.strftime("/%Y/%m/%d")
            yield scrapy.Request(
                f"http://api.proxiesapi.com/?auth_key=your_api_key&url=https://medium.com/topic/technology{date_str}",
                callback=self.parse
            )

    def parse(self, response):
        for entry in response.css('.streamItem'):

            yield {
                "title": entry.css('.graf--title::text').extract(),
                "claps": entry.css('.button[data-action="show-recommends"]::text').extract(),
                "author": entry.css('a[data-action="show-user-card"].ds-link::text').extract(),
            }
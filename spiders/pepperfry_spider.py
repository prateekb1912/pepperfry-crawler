import scrapy

class PepperFry(scrapy.Spider):
    name = 'pepperfry_spider'

    def start_requests(self):
        sofas_url = 'https://www.pepperfry.com/furniture-sofas.html'

        yield scrapy.Request(sofas_url, self.parse)

    def parse(self):
        pass

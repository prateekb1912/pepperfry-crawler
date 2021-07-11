import scrapy

class PepperFry(scrapy.Spider):
    name = 'pepperfry_spider'

    def start_requests(self):
        sofas_url = 'https://www.pepperfry.com/furniture-sofas.html'

        yield scrapy.Request(sofas_url, self.parse)

    def parse(self, response):
        sofa_divs = response.css('div.clip-crd-10x11')

        for sd in sofa_divs:
            sofa_name = sd.css('h2 a::text').get()
            sofa_price = sd.css('span.clip-offr-price::text').get()[2:]

            yield {
                'Model': sofa_name,
                'Price': sofa_price
            }

import scrapy


class BrazilCitiesSpider(scrapy.Spider):
    name = 'brazil'
    start_urls = ['https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o']

    def parse(self, response):
        for city in response.css('td a::text').getall():
            yield {
                'cities': city
            }

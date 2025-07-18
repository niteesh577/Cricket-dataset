import scrapy

class CricketSpider(scrapy.Spider):
    name = 'cricket'
    start_urls = ['https://www.pitchvision.com/front-foot-drive']

    def parse(self, response):
        content = response.css('div#content, main, article').xpath('string()').get()
        yield {
            'url': response.url,
            'text': content.strip()
        }

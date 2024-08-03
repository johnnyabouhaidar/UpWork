import scrapy

class BingSpider(scrapy.Spider):
    name = "bing"
    allowed_domains = ["bing.com"]
    start_urls = []

    def __init__(self, keyword=None, *args, **kwargs):
        super(BingSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword
        if self.keyword:
            self.start_urls = [f"https://www.bing.com/search?q={self.keyword}"]

    def parse(self, response):
        for result in response.xpath('//li[@class="b_algo"]//h2/a'):
            url = result.xpath('@href').get()
            if url:
                yield {'url': url}

        next_page = response.xpath('//a[@title="Next page"]/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
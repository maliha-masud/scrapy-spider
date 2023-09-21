import scrapy


class I202606UrduStoriesSpiderSpider(scrapy.Spider):
    name = "I202606_urdu_stories_spider"
    allowed_domains = ["urduzone.net"]
    start_urls = ["https://urduzone.net"]  #Start URL set

    def parse(self, response):
        pass

import scrapy

class UrduStoriesSpiderSpider(scrapy.Spider):
    name = "urdu_stories_spider"
    allowed_domains = ["urduzone.net"]
    start_urls = ['https://www.urduzone.net/?s=+']  #set the start URL: this search result lists all stories on the website

    def parse(self, response):
        stories = response.css('div.td_module_16.td_module_wrap.td-animation-stack')

        for story in stories:
            #extract properties to store
            title = story.css('h3.entry-title.td-module-title a::attr(title)').get()
            date = story.css('span.td-post-date time::text').get()
            link = story.css('h3.entry-title.td-module-title a::attr(href)').get()

            #navigate to the link of the story
            yield response.follow(link, self.parse_story, meta={'title': title, 'date': date})

            #extract link to next page
            next_page = response.css('a[aria-label="next-page"]::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, self.parse)

    def parse_story(self, response):
        #extract text content from the story page
        title = response.meta['title']
        date = response.meta['date']
        text_content = response.css('div.td_block_wrap.tdb_single_smartlist.tdi_32.td-pb-border-top.td_block_template_1.td-post-content.tagdiv-type p::text').getall()

        #store extracted data
        yield {
            'title': title,
            'date': date,
            'text_content': ' '.join(text_content)
        }
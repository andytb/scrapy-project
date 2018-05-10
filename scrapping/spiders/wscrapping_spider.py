import scrapy, psycopg2, datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class wscrappingSpider(CrawlSpider):
    name = "wscrapping"

    def __init__(self, **kw):
        super(wscrappingSpider, self).__init__(self, **kw)
        
        self.allowed_domains = kw.get('allowed_domains')
        self.start_urls = kw.get('start_urls')
        self.keywords = kw.get('keywords')
        self.rules = kw.get('rules')
        self.conn = kw.get('db')
    
    def parse_item(self, response):
        date = datetime.datetime.now()
        cur = self.conn.cursor()
        for keyword in self.keywords:
            title = response.xpath('//body//*[not(self::script)]/text()').re(r'.*' + keyword + '.*')
            for item in title:
                cur.execute("INSERT INTO output (keyword, info, date, source) VALUES (%s, %s, %s, %s)",
                (keyword, item, date, response.request.url))

        self.conn.commit()
        cur.close()
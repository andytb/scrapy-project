import scrapy, psycopg2, datetime
from urlparse import urlparse

class scrappingSpider(scrapy.Spider):
    name = "scrapping"

    def __init__(self, **kw):
        self.urls = kw.get('domains')
        self.keywords = kw.get('keywords')
        self.conn = kw.get('db')
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        date = datetime.datetime.now()
        cur = self.conn.cursor()
        for keyword in self.keywords:
            title = response.xpath('//body//*[not(self::script)]/text()').re(r'.*' + keyword + '.*')
            for item in title:
                cur.execute("INSERT INTO output (keyword, info, date, source) VALUES (%s, %s, %s, %s)",
                (keyword, item, date, response.request.url))

        self.conn.commit()
        cur.close()
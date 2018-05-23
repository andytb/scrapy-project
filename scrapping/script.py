#!/usr/bin/env python

import scrapy, psycopg2, spiders.wscrapping_spider as mySpider
import config.config as config, config.database as db
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

process = CrawlerProcess({
    'USER_AGENT': config.Config.USER_AGENT,
    'DOWNLOAD_DELAY': 2,
    'RETRY_ENABLED': False,
    'COOKIES_ENABLED': False,
    'REDIRECT_ENABLED': False,
    'AJAXCRAWL_ENABLED': True
})

conn_string = "host='" + db.DatabaseConfig.DB_HOST + "' "
conn_string += "dbname='" + db.DatabaseConfig.DB_NAME + "' "
conn_string += "user='" + db.DatabaseConfig.DB_USER + "'"
conn_string += "password='" + db.DatabaseConfig.DB_PASSWORD + "'"
conn = psycopg2.connect(conn_string)

rules = ( Rule(LinkExtractor(), callback='parse_item', follow=True), )

process.crawl(mySpider.wscrappingSpider, 
    db=conn,
    allowed_domains = config.Config.DOMAINS_TO_SCRAP,
    keywords = config.Config.KEYWORDS_FILTER,
    start_urls = config.Config.URLS_TO_SCRAP,
    rules = rules)
process.start()

conn.close()
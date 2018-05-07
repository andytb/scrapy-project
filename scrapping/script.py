import scrapy, psycopg2, spiders.scrapping_spider as mySpider
import config.config as config, config.database as db
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess({
    'USER_AGENT': config.Config.USER_AGENT
})

conn_string = "host='" + db.DatabaseConfig.DB_HOST + "' "
conn_string += "dbname='" + db.DatabaseConfig.DB_NAME + "' "
conn_string += "user='" + db.DatabaseConfig.DB_USER + "'"
conn_string += "password='" + db.DatabaseConfig.DB_PASSWORD + "'"
conn = psycopg2.connect(conn_string)

process.crawl(mySpider.scrappingSpider, 
    domains=config.Config.URLS_TO_SCRAP,
    db=conn, 
    keywords=config.Config.KEYWORDS_FILTER)
process.start()

conn.close()
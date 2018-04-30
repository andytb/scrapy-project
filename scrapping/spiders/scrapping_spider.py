import scrapy, psycopg2, datetime
import config, database

class scrappingSpider(scrapy.Spider):
    name = "scrapping"
    start_urls = config.Config.URLS_TO_SCRAP
    def parse(self, response):
        date = datetime.datetime.now()
        conn_string = "host='" + database.DatabaseConfig.DB_HOST + "' "
        conn_string += "dbname='" + database.DatabaseConfig.DB_NAME + "' "
        conn_string += "user='" + database.DatabaseConfig.DB_USER + "'"
        conn_string += "password='" + database.DatabaseConfig.DB_PASSWORD + "'"
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        for keyword in config.Config.KEYWORDS_FILTER:
            title = response.xpath('//body//*[not(self::script)]/text()').re(r'.*' + keyword + '.*')
            for item in title:
                cur.execute("INSERT INTO output (keyword, info, date, source) VALUES (%s, %s, %s, %s)",
                (keyword, item, date, response.request.url))

        conn.commit()
        cur.close()
        conn.close()

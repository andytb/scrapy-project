
# Scrapy Project
Simple program to scrape a web page looking for sentences that contain certain keywords, and storing these sentences in a PostgreSQL database.

### Prerequisites
To get the project running, you'd need:
```
PostgreSQL
Python 2.7
```

### Setting up the database
Create a PostgreSQL database and grant your user all privileges.
```sh
sudo -u postgres createdb db_name
sudo -u postgres psql
```
```sql
GRANT ALL PRIVILEGES ON DATABASE db_name TO user_name;
```

## To run
To install the necessary packages, use `pip` and run:

```sh
pip install scrapy
pip install datetime
pip install psycopg2
```

### Run the spider
To run the spider:
```sh
scrapy crawl scrapping
```
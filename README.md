
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
Create the table to store the program output.
```sql
CREATE TABLE output (
    output_id serial PRIMARY KEY,
    keyword varchar (100),
    info text,
    date date,
    source varchar (500)
);
```

### Installing
To install the necessary packages, use `pip` and run:

```sh
pip install scrapy
pip install datetime
pip install psycopg2
```

### Run the program
To run the program:
```sh
python script.py
```

### Config files
The database's and program's config files are located in the config folder.

#### Database configuration
PostgreSQL needs to be running, and the table *output* described previously needs to be created. The program also needs access to the database. The configuration variables are located in the *database.py* file. Change the following variables before running the script:

```python
    DB_NAME = 'db_name'
    DB_USER = 'db_user'
    DB_HOST = 'db_host'
    DB_PASSWORD = 'secret'
```
#### Crawler configuration
By default, the user agent to make the request, the URLs to scrap, the allowed domains and the keywords are all located in the *config.py*:

```python
    USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    URLS_TO_SCRAP = [
        'http://quotes.toscrape.com/page/1/'
    ]
    DOMAINS_TO_SCRAP = [
        'toscrape.com'
    ]
    KEYWORDS_FILTER = [
        'Harry', 
        'value',
        'love'
    ]
```
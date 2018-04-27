import psycopg2

user ='scrapping'
password = '123456'

conn = psycopg2.connect("dbname='scrapping' user='scrapping' host='localhost' password='password'")
cur = conn.cursor()
cur.execute("""SELECT * FROM output""")
rows = cur.fetchall()
print "\nShow me the databases:\n"
for row in rows:
    print row

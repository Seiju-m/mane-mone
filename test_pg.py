import psycopg2

conn = psycopg2.connect("host=127.0.0.1 port=5432 dbname=todo user=postgres password=Seiju7479")
cur = conn.cursor()
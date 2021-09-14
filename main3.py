import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="vocabulary_board",
    user="postgres",
    password="postgres")




import psycopg2

conn = psycopg2.connect(
    database="avecoder",
    user="postgres",
    password="wbtbwtb1",
    host="127.0.0.1",
    port="5432"
)

print("Database opened successfully")
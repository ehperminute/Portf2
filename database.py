import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="sales_db",
        user="user",
        password="password",
        host="127.0.0.1",
        port="5432",
    )

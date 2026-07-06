from contextlib import closing
import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="sales_db",
        user="user",
        password="password",
        host="127.0.0.1",
        port="5432",
        )


def fetch_all(query, params=None):
    with closing(get_connection()) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
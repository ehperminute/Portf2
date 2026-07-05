from database import get_connection
from psycopg2 import sql
from table_config import TABLES, generate_all_data


def reset_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        TRUNCATE sales, customers, products
        RESTART IDENTITY CASCADE;
    """)

    conn.commit()
    cursor.close()
    conn.close()


def insert_db(table, columns, data):
    if not data:
        return

    placeholders = sql.SQL(", ").join(sql.Placeholder() * len(columns))

    query = sql.SQL("""
        INSERT INTO {table} ({columns})
        VALUES ({placeholders})
    """).format(
        table=sql.Identifier(table),
        columns=sql.SQL(", ").join(map(sql.Identifier, columns)),
        placeholders=placeholders,
    )

    conn = get_connection()
    cursor = conn.cursor()
    cursor.executemany(query, data)
    conn.commit()
    cursor.close()
    conn.close()


def load_all():
    reset_tables()
    all_data = generate_all_data()

    for table_config in TABLES:
        table_name = table_config["name"]
        columns = table_config["columns"]
        data = all_data[table_name]

        insert_db(table_name, columns, data)


if __name__ == "__main__":
    load_all()
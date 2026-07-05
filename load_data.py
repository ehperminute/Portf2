from database import get_connection
from generate_customers import gen_customers
from generate_sales import gen_sales
from catalog import products
from psycopg2 import sql


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


products_with_ids = [
    (id, *product)
    for id, product in enumerate(products, start=1)
]

customers = gen_customers()

for table, columns, data in (
                            ("products", ["id", "name", "category", "price"], products_with_ids), 
                            ("customers", ["id", "country", "segment", "registration_date"], customers),
                            ("sales", ["id", "customer_id", "product_id", "quantity", "sale_date"], gen_sales(customers))
        
                            ):
    insert_db(table, columns, data)
from database import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("""
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price NUMERIC NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    country TEXT NOT NULL,
    segment TEXT NOT NULL,
    registration_date DATE NOT NULL
);
""")

CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    product_id INTEGER NOT NULL REFERENCES products(id),
    quantity INTEGER NOT NULL,
    sale_date DATE NOT NULL
);""")





conn.commit()
conn.close()

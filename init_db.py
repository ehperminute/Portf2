from database import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("""

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price NUMERIC NOT NULL CHECK (price > 0)
);
""")
               
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    country TEXT NOT NULL,
    segment TEXT NOT NULL CHECK (segment IN ('Consumer', 'Small Business', 'Enterprise')),
    registration_date DATE NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    product_id INTEGER NOT NULL REFERENCES products(id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    sale_date DATE NOT NULL
);
""")





conn.commit()
conn.close()

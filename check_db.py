from database import get_connection

conn = get_connection()
cursor = conn.cursor()

for table in ["products", "customers", "sales"]:
    cursor.execute(f"SELECT COUNT(*) FROM {table};")
    count = cursor.fetchone()[0]
    print(table, count)

cursor.close()
conn.close()
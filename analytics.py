from database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
    SELECT 
        p.category,
        SUM(s.quantity * p.price) AS revenue
    FROM sales s
    JOIN products p ON s.product_id = p.id
    GROUP BY p.category
    ORDER BY revenue DESC;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()

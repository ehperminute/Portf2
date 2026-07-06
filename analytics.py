from database import fetch_all

rows = fetch_all("""
    SELECT 
    p.name,
    p.category,
    SUM(s.quantity * p.price) AS revenue
    FROM sales s
    JOIN products p ON s.product_id = p.id
    GROUP BY p.name, p.category
    ORDER BY revenue DESC;
    """)

for name, category, revenue in rows:
    print(f"{name} ({category}): ${revenue:,.2f}")
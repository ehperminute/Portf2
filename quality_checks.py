from database import get_connection

conn = get_connection()
cursor = conn.cursor()

checks = [
    (
        "No sales with quantity <= 0",
        """
        SELECT COUNT(*)
        FROM sales
        WHERE quantity <= 0;
        """
    ),
    (
        "No products with price <= 0",
        """
        SELECT COUNT(*)
        FROM products
        WHERE price <= 0;
        """
    ),
    (
        "No sales with missing customers",
        """
        SELECT COUNT(*)
        FROM sales s
        LEFT JOIN customers c ON s.customer_id = c.id
        WHERE c.id IS NULL;
        """
    ),
    (
        "No sales with missing products",
        """
        SELECT COUNT(*)
        FROM sales s
        LEFT JOIN products p ON s.product_id = p.id
        WHERE p.id IS NULL;
        """
    ),
    (
        "No sale before customer registration date",
        """
        SELECT COUNT(*)
        FROM sales s
        JOIN customers c ON s.customer_id = c.id
        WHERE s.sale_date < c.registration_date;
        """
    ),
    (
        "No invalid customer segments",
        """
        SELECT COUNT(*)
        FROM customers
        WHERE segment NOT IN ('Consumer', 'Small Business', 'Enterprise');
        """
    ),
]

for name, query in checks:
    cursor.execute(query)
    problems = cursor.fetchone()[0]

    if problems == 0:
        print(f"PASS - {name}")
    else:
        print(f"FAIL - {name}: {problems} problems found")

cursor.close()
conn.close()            



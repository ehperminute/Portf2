from database import fetch_one


def run_check(name, query):
    result = fetch_one(query)[0]

    if result == 0:
        print(f"PASS - {name}")
    else:
        print(f"FAIL - {name}: {result} problems found")


run_check(
    "No sales with quantity <= 0",
    """
    SELECT COUNT(*)
    FROM sales
    WHERE quantity <= 0;
    """
)

run_check(
    "No products with price <= 0",
    """
    SELECT COUNT(*)
    FROM products
    WHERE price <= 0;
    """
)

run_check(
    "No sales with missing customers",
    """
    SELECT COUNT(*)
    FROM sales s
    LEFT JOIN customers c ON s.customer_id = c.id
    WHERE c.id IS NULL;
    """
)

run_check(
    "No sales with missing products",
    """
    SELECT COUNT(*)
    FROM sales s
    LEFT JOIN products p ON s.product_id = p.id
    WHERE p.id IS NULL;
    """
)

run_check(
    "No sale before customer registration date",
    """
    SELECT COUNT(*)
    FROM sales s
    JOIN customers c ON s.customer_id = c.id
    WHERE s.sale_date < c.registration_date;
    """
)

run_check(
    "No invalid customer segments",
    """
    SELECT COUNT(*)
    FROM customers
    WHERE segment NOT IN ('Consumer', 'Small Business', 'Enterprise');
    """
)

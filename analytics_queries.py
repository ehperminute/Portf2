QUERIES = {
    "revenue_by_product": """
        SELECT 
            p.name,
            p.category,
            SUM(s.quantity * p.price) AS revenue
        FROM sales s
        JOIN products p ON s.product_id = p.id
        GROUP BY p.name, p.category
        ORDER BY revenue DESC;
    """,

    "revenue_by_category": """
        SELECT 
            p.category,
            SUM(s.quantity * p.price) AS revenue
        FROM sales s
        JOIN products p ON s.product_id = p.id
        GROUP BY p.category
        ORDER BY revenue DESC;
    """,

    "revenue_by_country": """
        SELECT
            c.country,
            SUM(s.quantity * p.price) AS revenue
        FROM sales s
        JOIN customers c ON s.customer_id = c.id
        JOIN products p ON s.product_id = p.id
        GROUP BY c.country
        ORDER BY revenue DESC;
    """,

    "monthly_revenue": """
        SELECT
            DATE_TRUNC('month', s.sale_date)::date AS month,
            SUM(s.quantity * p.price) AS revenue
        FROM sales s
        JOIN products p ON s.product_id = p.id
        GROUP BY month
        ORDER BY month;
    """,

    "top_customers": """
        SELECT
            c.id AS customer_id,
            c.country,
            c.segment,
            SUM(s.quantity * p.price) AS revenue
        FROM sales s
        JOIN customers c ON s.customer_id = c.id
        JOIN products p ON s.product_id = p.id
        GROUP BY c.id, c.country, c.segment
        ORDER BY revenue DESC
        LIMIT 20;
    """
}

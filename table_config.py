from catalog import products
from generate_customers import gen_customers
from generate_sales import gen_sales


def get_products_with_ids():
    return [
        (id, *product)
        for id, product in enumerate(products, start=1)
    ]


def generate_all_data():
    customers = gen_customers()
    sales = gen_sales(customers)

    return {
        "products": get_products_with_ids(),
        "customers": customers,
        "sales": sales,
    }


TABLES = [
    {
        "name": "products",
        "columns": ["id", "name", "category", "price"],
    },
    {
        "name": "customers",
        "columns": ["id", "country", "segment", "registration_date"],
    },
    {
        "name": "sales",
        "columns": ["id", "customer_id", "product_id", "quantity", "sale_date"],
    },
]
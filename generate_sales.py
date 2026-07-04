import random
from generate_customers import N_CUSTOMERS
from catalog.py import products



N_SALES = 10000


start = datetime.date(2023, 1, 1)
end = datetime.date(2025, 12, 31)
delta = end - start


def gen_sales():
    sales = []
    customers = gen_customers
    for sale_id in range(1, N_SALES + 1):
        
        customer_id = random.randint(1, N_CUSTOMERS)
        product_id = random.randint(1, len(products))

        random_days = random.randint(delta.days + 1)
        sale_date = start + datetime.timedelta(days=random_days)
        quantity = random.randint(1, 5)
        sales.append((sale_id, customer_id, product_id, sale_date))

    print(sales[:10])
    return sales

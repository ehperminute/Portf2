import random
import datetime
from generate_customers import N_CUSTOMERS, gen_customers
from catalog import products

N_SALES = 10000
END_DATE = datetime.date(2025, 12, 31)

def gen_sales():
    sales = []
    customers = gen_customers()

    for sale_id in range(1, N_SALES + 1):
        customer_id = random.randint(1, N_CUSTOMERS)
        customer = customers[customer_id - 1]
        registration_date = customer[3]

        product_id = random.randint(1, len(products))

        delta = END_DATE - registration_date
        random_days = random.randrange(delta.days + 1)
        sale_date = registration_date + datetime.timedelta(days=random_days)

        quantity = random.randint(1, 5)

        sales.append((sale_id, customer_id, product_id, quantity, sale_date))

    print(sales[:10])
    return sales

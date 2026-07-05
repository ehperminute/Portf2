import random
import datetime
from generate_customers import N_CUSTOMERS, gen_customers
from catalog import products, category_weights

N_SALES = 10000
END_DATE = datetime.date(2025, 12, 31)

product_weights = [
    category_weights[category]
    for name, category, price in products
]

def gen_sales(customers=None):
    sales = []
    if customers is None:
        customers = gen_customers()
    chosen_products = random.choices(
    range(1, len(products)+1),
    weights=product_weights,
    k=N_SALES
)

    for sale_id, product_id in enumerate(chosen_products, start=1):
        customer_id = random.randint(1, len(customers))
        customer = customers[customer_id - 1]
        registration_date = customer[3]

        delta = END_DATE - registration_date
        random_days = random.randrange(delta.days + 1)
        sale_date = registration_date + datetime.timedelta(days=random_days)

        quantity = random.randint(1, 5)

        sales.append((sale_id, customer_id, product_id, quantity, sale_date))

    return sales

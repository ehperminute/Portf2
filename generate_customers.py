import random
import datetime

N_CUSTOMERS = 1000

countries = [
    "Mexico", "Brazil", "USA", "Colombia", "Chile",
    "Argentina", "Peru", "Canada", "Dominican Republic",
    "Costa Rica", "Guatemala"
]

country_weights = [35, 20, 15, 8, 5, 5, 4, 4, 2, 1, 1]

segments = ["Consumer", "Small Business", "Enterprise"]
segment_weights = [78, 18, 4]

start = datetime.date(2023, 1, 1)
end = datetime.date(2025, 12, 31)
delta = end - start

customers = []
def gen_customers():
    for customer_id in range(1, N_CUSTOMERS + 1):
        country = random.choices(countries, weights=country_weights, k=1)[0]
        segment = random.choices(segments, weights=segment_weights, k=1)[0]

        random_days = random.randrange(delta.days + 1)
        registration_date = start + datetime.timedelta(days=random_days)

        customers.append((customer_id, country, segment, registration_date))

    return customers

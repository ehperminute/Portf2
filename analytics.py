from database import fetch_all
from analytics_queries import QUERIES


rows = fetch_all(QUERIES["revenue_by_product"])

for name, category, revenue in rows:
    print(f"{name} ({category}): ${revenue:,.2f}")

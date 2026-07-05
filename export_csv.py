import csv
from generate_customers import gen_customers
from generate_sales import gen_sales
from catalog import products


def export(filename, data):
    with open(filename, "w", encoding="utf8") as out_f:
        writer = csv.writer(out_f)
        writer.writerows(data)


for data, filename in (products, "products.csv"), (gen_sales(), "sales.csv"), (gen_cudtomers(), "customers.csv"):
    export(filename, data)

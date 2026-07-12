from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


REPORTS_DIR = Path("reports")
CHARTS_DIR = Path("dashboard/screenshots")
CHARTS_DIR.mkdir(parents=True, exist_ok=True)


def save_revenue_by_category():
    df = pd.read_csv(REPORTS_DIR / "revenue_by_category.csv")
    df["revenue"] = pd.to_numeric(df["revenue"])

    df = df.sort_values("revenue", ascending=True)

    plt.figure(figsize=(10, 6))
    plt.barh(df["category"], df["revenue"])
    plt.title("Revenue by Category")
    plt.xlabel("Revenue")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "revenue_by_category.png")
    plt.close()


def save_top_products():
    df = pd.read_csv(REPORTS_DIR / "revenue_by_product.csv")
    df["revenue"] = pd.to_numeric(df["revenue"])

    df = df.sort_values("revenue", ascending=False).head(10)
    df = df.sort_values("revenue", ascending=True)

    plt.figure(figsize=(10, 6))
    plt.barh(df["name"], df["revenue"])
    plt.title("Top 10 Products by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Product")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "top_products_by_revenue.png")
    plt.close()


def save_revenue_by_country():
    df = pd.read_csv(REPORTS_DIR / "revenue_by_country.csv")
    df["revenue"] = pd.to_numeric(df["revenue"])

    df["revenue_millions"] = df["revenue"] / 1_000_000

    df = df.sort_values("revenue_millions", ascending=True)

    plt.figure(figsize=(10, 6))
    plt.barh(df["country"], df["revenue_millions"])
    plt.title("Revenue by Country")
    plt.xlabel("Revenue (millions MXN)")
    plt.ylabel("Country")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "revenue_by_country.png")
    plt.close()


def save_monthly_revenue():
    df = pd.read_csv(REPORTS_DIR / "monthly_revenue.csv")
    df["month"] = pd.to_datetime(df["month"])
    df["revenue"] = pd.to_numeric(df["revenue"])

    df = df.sort_values("month")

    plt.figure(figsize=(12, 6))
    plt.plot(df["month"], df["revenue"], marker="o")
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "monthly_revenue.png")
    plt.close()


def main():
    save_revenue_by_category()
    save_top_products()
    save_revenue_by_country()
    save_monthly_revenue()

    print(f"Charts saved to {CHARTS_DIR}")


if __name__ == "__main__":
    main()

import csv
from pathlib import Path

from database import get_connection
from analytics_queries import QUERIES


REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)


def export_report(cursor, report_name, query):
    cursor.execute(query)

    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()

    filepath = REPORTS_DIR / f"{report_name}.csv"

    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(rows)

    print(f"Exported {filepath}")


def main():
    conn = get_connection()
    cursor = conn.cursor()

    for report_name, query in QUERIES.items():
        export_report(cursor, report_name, query)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()

from database import get_connection


PROMPT = "mini_psql> "


def list_tables(cursor):
    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name;
    """)

    rows = cursor.fetchall()

    for row in rows:
        print(row[0])


def describe_table(cursor, table_name):
    cursor.execute("""
        SELECT
            column_name,
            data_type,
            is_nullable
        FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = %s
        ORDER BY ordinal_position;
    """, (table_name,))

    rows = cursor.fetchall()

    if not rows:
        print(f"Table not found: {table_name}")
        return

    print(f"Table: {table_name}")
    for column_name, data_type, is_nullable in rows:
        print(f"{column_name:25} {data_type:20} nullable: {is_nullable}")


def execute_sql(cursor, conn, query):
    try:
        cursor.execute(query)

        if cursor.description:
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()

            print(columns)
            for row in rows:
                print(row)
        else:
            conn.commit()
            print(f"Query executed. Rows affected: {cursor.rowcount}")

    except Exception as e:
        conn.rollback()
        print("ERROR:")
        print(e)


def main():
    conn = get_connection()
    cursor = conn.cursor()

    sql_buffer = ""

    print("Tiny PostgreSQL shell")
    print("Commands: \\dt, \\d table_name, \\q")

    while True:
        line = input(PROMPT)

        stripped = line.strip()

        if stripped == "\\q":
            break

        if stripped == "\\dt":
            list_tables(cursor)
            continue

        if stripped.startswith("\\d "):
            table_name = stripped.split(maxsplit=1)[1]
            describe_table(cursor, table_name)
            continue

        sql_buffer += line + "\n"

        if not stripped.endswith(";"):
            continue

        query = sql_buffer.strip()
        execute_sql(cursor, conn, query)
        sql_buffer = ""

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()

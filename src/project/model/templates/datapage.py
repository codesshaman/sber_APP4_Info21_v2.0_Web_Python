from model.database.sql_query import (
    fetchall_query,
    update_query,
    drop_query
)

import sys


def table_titles(table_name: str) -> tuple:
    arr = fetchall_query(
        f"SELECT column_name FROM information_schema.columns "
        f"WHERE table_name = '{table_name}' ORDER BY ordinal_position;"
    )
    return arr


def table_rows(table: str) -> tuple:
    arr = fetchall_query(f"SELECT * FROM {table} ORDER BY 1;")
    return arr


def all_tables():
    arr = fetchall_query(
        "SELECT table_name FROM information_schema.tables "
        "WHERE table_schema NOT IN ('information_schema','pg_catalog');"
    )
    return arr


def drop_table(table_name: str) -> tuple:
    return drop_query(f"DROP TABLE {table_name} CASCADE;")


def save_table(table_name: str) -> None:
    fetchall_query(
        f"""CALL pr_export_to_csv_from_table('{table_name}',
        '/var/lib/postgresql/output/{table_name}.csv', ',');
        """
    )


def import_table(table_name: str) -> None:
    print(table_name, file=sys.stderr)
    update_query(
        f"""TRUNCATE {table_name} CASCADE;
        CALL pr_import_from_csv_to_table('{table_name}',
        '/var/lib/postgresql/output/{table_name}.csv', ',');
        """
    )


def delete_row_query(table_name: str, row: list) -> tuple:
    fields = table_titles(table_name)

    conditions = []
    for field, r in zip(fields, row):
        if str(r).isdigit():
            conditions.append(f'{table_name}."{field[0]}" = {r}')
        elif r is None:
            conditions.append(f'{table_name}."{field[0]}" IS NULL')
        else:
            conditions.append(f"{table_name}.\"{field[0]}\" = '{r}'")

    conditions = " AND ".join(conditions)
    query = f"DELETE FROM {table_name} WHERE {conditions};"

    return drop_query(query)


def insert_row_query(table_name: str, row: dict) -> tuple:
    # fields = "', '".join([key for key in row.keys()])
    values = "', '".join(
        [value for key, value in row.items() if key != "table_name"]
    )
    query = f"""INSERT INTO {table_name}
                VALUES ('{values}');
                """
    return update_query(query)


def update_row_query(table_name: str, row: list, new_row: list) -> tuple:
    fields = table_titles(table_name)

    conditions = []
    values = []
    for field, r, nr in zip(fields, row, new_row):
        if str(r).isdigit():
            conditions.append(f'"{field[0]}" = {r}')
            values.append(f'"{field[0]}" = {nr}')
        elif r is None:
            conditions.append(f'"{field[0]}" IS NULL')
            values.append(f'"{field[0]}" = NULL')
        else:
            conditions.append(f"\"{field[0]}\" = '{r}'")
            values.append(f"\"{field[0]}\" = '{nr}'")

    conditions = " AND ".join(conditions)
    values = ", ".join(values)
    query = f"UPDATE {table_name} SET {values} WHERE {conditions};"

    return update_query(query)

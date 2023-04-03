from model.database.sql_query import *

def table_titles(table):
    arr = fetchall_query(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}' ORDER BY ordinal_position;")
    return arr


def table_rows(table):
    return fetchall_query(f"SELECT * FROM {table};")

def all_tables():
    arr = fetchall_query("SELECT table_name FROM information_schema.tables "
                         "WHERE table_schema NOT IN ('information_schema','pg_catalog');")
    return arr

def drop_table(table_name):
    return drop_query(f"DROP TABLE {table_name} CASCADE;")


def all_links():
    arr = all_tables()
    res = []
    i = 0
    try:
        while i < len(arr):
            link = '"' + arr[i][2] + '.html"'
            res.append(link)
            i += 1
    except:
        res = []
    return res

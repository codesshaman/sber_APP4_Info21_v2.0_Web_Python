from model.database.sql_query import *

def table_titles(table):
    arr = fetchall_query("SELECT column_name FROM "
                         "information_schema.columns WHERE table_name = '" +
                         table + "' ORDER BY ordinal_position;")
    return arr


def table_rows(table):
    return fetchall_query("SELECT * FROM public." + table + " ORDER BY nickname ASC;")

def all_tables():
    arr = fetchall_query("SELECT * FROM information_schema.tables "
                         "WHERE table_schema NOT IN "
                         "('information_schema','pg_catalog');")
    return arr
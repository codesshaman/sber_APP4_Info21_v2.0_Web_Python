from model.database.sql_query import *

def table_data():
    return fetchall_query("SELECT * FROM public.peers ORDER BY nickname ASC;")
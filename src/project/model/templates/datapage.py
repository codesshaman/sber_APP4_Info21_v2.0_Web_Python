from model.database.sql_query import sql_query

def table_data():
    return sql_query("SELECT * FROM recommendations;")
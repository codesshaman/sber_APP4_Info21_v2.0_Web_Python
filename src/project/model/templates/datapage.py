from controllers.db_connection import sql_execute

def table_data():
    data = sql_execute("""SELECT Nickname FROM Peers;""")
    return data

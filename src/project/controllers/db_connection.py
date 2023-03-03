from all_path import above_directory
import psycopg2, os, sys
sys.path.insert(above_directory)
from ..config import host, user, pwd, db_name


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=pwd,
        database=db_name
    )
    connection.autocommit = True

    cur = connection.cursor()

    cur.execute("SELECT version();")
    print(f"Server version: {cur.fetchone()}")

    cur.execute("SELECT version();")
    print(f"Server version: {cur.fetchone()}")

    cur.execute("""SELECT Nickname FROM Peers;""")
    print(cur.fetchone())


except Exception as _ex:
    print("[INFO] Cannot connect to the database!", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] Database connection closed")

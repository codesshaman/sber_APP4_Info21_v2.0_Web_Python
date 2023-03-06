from model.database.connection import parse_config
import psycopg2


def sql_query(sql):
    "Функция подключения к базе"
    connection = None
    result = None
    try:
        params = parse_config()
        connection = psycopg2.connect(**params)
        cur = connection.cursor()
        cur.execute(sql)
        query_result = cur.fetchone()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as err:
        print(err)
    finally:
        if connection is not None:
            connection.close()
            print('Connection terminated')
    return query_result
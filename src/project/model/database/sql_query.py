from model.database.connection import parse_config
import psycopg2, sys

def drop_query(sql):
    connection = None
    try:
        params = parse_config()
        connection = psycopg2.connect(**params)
        cur = connection.cursor()
        cur.execute(sql)
        cur.close()
        connection.commit()
    except(Exception, psycopg2.DatabaseError) as err:
        print(err, file=sys.stderr)
    finally:
        if connection is not None:
            connection.close()
            print('Connection terminated', file=sys.stderr)

def fetchone_query(sql):
    "Функция, возвращающая одну строку из базы"
    connection = None
    query_result = None
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

def fetchall_query(sql):
    "Функция, возвращающая все строки из базы"
    connection = None
    query_result = None
    try:
        params = parse_config()
        connection = psycopg2.connect(**params)
        cur = connection.cursor()
        cur.execute(sql)
        query_result = cur.fetchall()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as err:
        print(err)
    finally:
        if connection is not None:
            connection.close()
            print('Connection terminated')
    return query_result
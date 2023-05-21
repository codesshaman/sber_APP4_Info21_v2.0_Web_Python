from model.database.connection import parse_config
import psycopg2
import sys


def drop_query(sql: str) -> tuple:
    connection = None
    try:
        params = parse_config()
        connection = psycopg2.connect(**params)
        cur = connection.cursor()
        query_result = cur.execute(sql)
        cur.close()
        connection.commit()
    except (Exception, psycopg2.Error) as err:
        query_result = err.diag.message_detail
    finally:
        if connection is not None:
            connection.close()
    return query_result


def update_query(sql: str) -> tuple:
    connection = None
    try:
        params = parse_config()
        connection = psycopg2.connect(**params)
        cur = connection.cursor()
        query_result = cur.execute(sql)
        cur.close()
        connection.commit()
    except (Exception, psycopg2.Error) as err:
        query_result = err.diag.message_detail
        print(query_result, file=sys.stderr)
    finally:
        if connection is not None:
            connection.close()
    return query_result


def fetchone_query(sql: str) -> tuple:
    """Функция, возвращающая одну строку из базы"""
    connection = None
    try:
        params = parse_config()
        connection = psycopg2.connect(**params)
        cur = connection.cursor()
        cur.execute(sql)
        query_result = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.Error) as err:
        query_result = err.diag.message_detail
        print(query_result, file=sys.stderr)
    finally:
        if connection is not None:
            connection.close()
    return query_result


def fetchall_query(sql: str) -> tuple:
    """Функция, возвращающая все строки из базы"""
    connection = None
    try:
        params = parse_config()
        connection = psycopg2.connect(**params)
        cur = connection.cursor()
        cur.execute(sql)
        query_result = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.Error) as err:
        query_result = err.diag.message_detail
        print(query_result, file=sys.stderr)

    finally:
        if connection is not None:
            connection.close()
    return query_result

from configparser import ConfigParser
import psycopg2


def parse_config(filename="config.ini", section="postgresql"):
    "Считываем конфигурацию"
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} is not found in the {1} file'.format(section, filename))
    return db

def connect():
    "Функция подключения к базе"
    connection = None
    result = None
    try:
        params = parse_config()
        print('Connection to the DataBase')
        connection = psycopg2.connect(**params)

        cur = connection.cursor()
        print('Postgres version: ')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        result = db_version
        cur.close()
    except(Exception, psycopg2.DatabaseError) as err:
        print(err)
    finally:
        if connection is not None:
            connection.close()
            print('Connection terminated')
    return result
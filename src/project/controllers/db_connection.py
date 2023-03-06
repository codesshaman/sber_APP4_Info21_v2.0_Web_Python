from controllers.all_path import above_directory
import psycopg2, sys
sys.path.insert(0, above_directory)
from configparser import ConfigParser


def config(filename="config.ini", section="postgresql"):
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
    print(db)

class DbConnect():
    def __init__(self):
        super().__init__()
    self.host = config.host

def connect(host, user, pwd, db_name):
    try:
        print("try to connect")
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=pwd,
            database=db_name
        )
        # connection.autocommit = True
        print("get cursor")
        cur = connection.cursor()
    except Exception as _ex:
        print("[INFO] Cannot connect to the database!", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] Database connection closed")
    return cur

def sql_execute():
    "Функция, выполняющая sql-запросы"
    cur = connect(host, user, pwd, db_name)
    with cur as curs:
        curs.execute('SELECT Nickname FROM Peers;')
        result = curs.fetchall()
        return result
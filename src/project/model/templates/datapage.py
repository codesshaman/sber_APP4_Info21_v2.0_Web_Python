from model.database.sql_query import *


def table_titles(table):
    arr = fetchall_query(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}' ORDER BY ordinal_position;")
    list_arr = list(arr)
    list_arr.append(('action',))
    return list_arr


def table_rows(table):
    arr = fetchall_query(f"SELECT * FROM {table};")
    i = 0
    for string in arr:
        j = 0
        str_list = list(string)
        for el in str_list:
            elem = str_list[j]
            elem = [str(elem), str(i), str(j), "Ячейка для редактирования: "]
            str_list[j] = elem
            j+=1
        str_list.append(["удаление", str(i), str(j), "Подтвердите действие для строки: "])
        arr[i] = str_list
        i += 1
    return arr

def all_tables():
    arr = fetchall_query("SELECT table_name FROM information_schema.tables "
                         "WHERE table_schema NOT IN ('information_schema','pg_catalog');")
    return arr

def drop_table(table_name):
    return drop_query(f"DROP TABLE {table_name} CASCADE;")

from model.database.sql_query import fetchall_query


def select_all_functions() -> tuple:
    arr = fetchall_query(
        """SELECT p.proname
        FROM pg_catalog.pg_namespace n
        JOIN pg_catalog.pg_proc p ON p.pronamespace = n.oid
        WHERE n.nspname = 'public';"""
    )
    return arr


def custom_query(query) -> tuple:
    return fetchall_query(query)


def select_all_descriptions() -> list:
    arr = select_all_functions()
    res = []
    for obj in arr:
        element = fetchall_query(
            f"""
            SELECT description FROM pg_description
            WHERE objoid = '{obj[0]}'::regproc;
    """
        )
        res.append(element[0][0])
    return res


def dispaly_descr() -> list:
    titles = select_all_functions()
    keys = [t[0] for t in titles]
    values = select_all_descriptions()
    dic = dict(zip(keys, values))
    res = list(dic.items())
    return res

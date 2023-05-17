from django.db import connection

def query_to_dict(query_string, **kwargs):
    try:
        cursor = connection.cursor()
        cursor.execute(query_string)
        rows = cursor.fetchall()
    except Exception as e:
        return False, str(e)
    col_names = [desc[0] for desc in cursor.description]
    return True, [dict(zip(col_names, row)) for row in rows]

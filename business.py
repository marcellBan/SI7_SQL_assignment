'''
business logic for the SI8 SQL assignment
by night5word (Marcell Bán)
'''

import os
import psycopg2
from flask import abort


def connect_to_db(func):
    def wrapper(*args, **kwargs):
        connection_data = {
            'dbname': os.environ.get('MY_PSQL_DBNAME'),
            'user': os.environ.get('MY_PSQL_USER'),
            'host': os.environ.get('MY_PSQL_HOST'),
            'password': os.environ.get('MY_PSQL_PASSWORD')
        }
        if any(map(lambda x: x is None, connection_data.values())):
            abort(500, 'No database config found.')
        connect_string = "dbname='{dbname}' user='{user}' host='{host}' password='{password}'"
        connect_string = connect_string.format(**connection_data)
        try:
            global cursor
            connection = psycopg2.connect(connect_string)
            connection.autocommit = True
            cursor = connection.cursor()
            result = func(*args, **kwargs)
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            abort(500, e)
    return wrapper

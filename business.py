'''
business logic for the SI7 SQL assignment
by night5word (Marcell Bán)
'''

import psycopg2
import sys


def connect_to_db(connection_data):
    connect_string = "dbname='{dbname}' user='{user}' host='{host}' password='{password}'"
    connect_string = connect_string.format(**connection_data)
    try:
        connection = psycopg2.connect(connect_string)
        connection.autocommit = True
        return connection.cursor()
    except Exception as e:
        print(e, file=sys.stderr)
        return None


def first_task(cursor):
    pass


def second_task(cursor):
    pass


def third_task(cursor):
    pass


def fourth_task(cursor):
    pass


def fifth_task(cursor):
    pass


def sixth_task(cursor):
    pass


def seventh_task(cursor):
    pass

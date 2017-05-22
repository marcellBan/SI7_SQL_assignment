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


@connect_to_db
def mentors_and_schools():
    query = '''SELECT m.first_name, m.last_name, s.name, s.country
                 FROM mentors m
                 INNER JOIN schools s
                   ON m.city = s.city
                 ORDER BY m.id'''
    cursor.execute(query)
    results = cursor.fetchall()
    return {
        'title': 'Mentors and schools',
        'text': 'All mentors and their schools',
        'headers': [
            'First name', 'Last name', 'School name', 'School country'
        ],
        'table': results
    }


@connect_to_db
def all_schools():
    query = '''SELECT m.first_name, m.last_name, s.name, s.country
                 FROM mentors m
                 RIGHT OUTER JOIN schools s
                   ON m.city = s.city
                 ORDER BY m.id'''
    cursor.execute(query)
    results = cursor.fetchall()
    return {
        'title': 'Mentors and schools',
        'text': 'All mentors and all schools',
        'headers': [
            'First name', 'Last name', 'School name', 'School country'
        ],
        'table': results
    }


@connect_to_db
def mentors_by_country():
    query = '''SELECT s.country, COUNT(m.id) AS "count"
                 FROM mentors m
                 RIGHT OUTER JOIN schools s
                   ON m.city = s.city
                 GROUP BY s.country
                 ORDER BY s.country'''
    cursor.execute(query)
    results = cursor.fetchall()
    return {
        'title': 'Mentors and schools',
        'text': 'All mentors and their schools',
        'headers': [
            'Country', 'Mentor count'
        ],
        'table': results
    }


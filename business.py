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
                 ORDER BY m.id;'''
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
                 ORDER BY m.id;'''
    cursor.execute(query)
    results = cursor.fetchall()
    return {
        'title': 'All schools',
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
                 ORDER BY s.country;'''
    cursor.execute(query)
    results = cursor.fetchall()
    return {
        'title': 'Mentors by country',
        'text': 'Mentor count per country',
        'headers': [
            'Country', 'Mentor count'
        ],
        'table': results
    }


@connect_to_db
def contacts():
    query = '''SELECT s.name, m.first_name, m.last_name
                 FROM schools s
                 INNER JOIN mentors m
                   ON s.contact_person = m.id
                 ORDER BY s.name;'''
    cursor.execute(query)
    results = cursor.fetchall()
    return {
        'title': 'Contacts',
        'text': 'Contact names',
        'headers': [
            'School name', 'Contact first name', 'Contact last name'
        ],
        'table': results
    }


@connect_to_db
def applicants():
    query = '''SELECT a.first_name, a.application_code, am.creation_date
                 FROM applicants a
                 INNER JOIN applicants_mentors am
                   ON a.id = am.applicant_id
                 WHERE am.creation_date > '2016-01-01'
                 ORDER BY am.creation_date DESC;'''
    cursor.execute(query)
    results = cursor.fetchall()
    return {
        'title': 'Applicants',
        'text': 'All applicants after 2016-01-01',
        'headers': [
            'First name', 'Application code', 'Creation date'
        ],
        'table': results
    }


@connect_to_db
def applicants_and_mentors():
    query = '''SELECT a.first_name, a.application_code, m.first_name, m.last_name
                 FROM applicants a
                 LEFT OUTER JOIN applicants_mentors am
                   ON a.id = am.applicant_id
                 LEFT OUTER JOIN mentors m
                   ON am.mentor_id = m.id
                 ORDER BY a.id;'''
    cursor.execute(query)
    results = cursor.fetchall()
    return {
        'title': 'Applicants and mentors',
        'text': 'All applicants and their mentors',
        'headers': [
            'Applicant first name', 'Application code', 'Mentor first name', 'Mentor last name'
        ],
        'table': results
    }

'''
business logic for the SI7 SQL assignment
by night5word (Marcell Bán)
'''

import psycopg2
import sys
import ui


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
    query = "SELECT first_name, last_name FROM mentors"
    cursor.execute(query)
    results = cursor.fetchall()
    pretext = ui.get_separator()
    pretext += '\nFirst task:\n'
    pretext += ui.get_separator()
    pretext += '\nFirst and last names of all the mentors'
    ui.display_results_table(pretext, ('First name', 'Last name'), results)


def second_task(cursor):
    query = "SELECT nick_name FROM mentors WHERE city='Miskolc'"
    cursor.execute(query)
    results = cursor.fetchall()
    pretext = ui.get_separator()
    pretext += '\nSecond task:\n'
    pretext += ui.get_separator()
    pretext += '\nNicknames of the mentors located at Miskolc'
    ui.display_results_table(pretext, ('Nickname',), results)


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

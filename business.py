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
    query = "SELECT CONCAT_WS(' ', first_name, last_name) AS full_name, phone_number "
    query += "FROM applicants WHERE first_name='Carol'"
    cursor.execute(query)
    results = cursor.fetchall()
    pretext = ui.get_separator()
    pretext += '\nThird task:\n'
    pretext += ui.get_separator()
    pretext += '\nFull name and phone number of Carol'
    ui.display_results_table(pretext, ('Full name', 'Phone number'), results)


def fourth_task(cursor):
    query = "SELECT CONCAT_WS(' ', first_name, last_name) AS full_name, phone_number "
    query += "FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu'"
    cursor.execute(query)
    results = cursor.fetchall()
    pretext = ui.get_separator()
    pretext += '\nFourth task:\n'
    pretext += ui.get_separator()
    pretext += '\nFull name and phone number of the other girl'
    ui.display_results_table(pretext, ('Full name', 'Phone number'), results)


def fifth_task(cursor):
    query = "INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) "
    query += "VALUES (%s, %s, %s, %s, %s)"
    data = ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823)
    cursor.execute(query, data)
    query = "SELECT * FROM applicants WHERE application_code=54823"
    cursor.execute(query)
    results = cursor.fetchall()
    pretext = ui.get_separator()
    pretext += '\nFifth task:\n'
    pretext += ui.get_separator()
    pretext += '\nInserted the new applicant below'
    ui.display_results_table(pretext,
                             ('ID', 'First name', 'Last name', 'Phone number', 'Email', 'Application code'),
                             results)


def sixth_task(cursor):
    pass


def seventh_task(cursor):
    pass

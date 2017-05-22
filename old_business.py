'''
business logic for the SI7 SQL assignment
by night5word (Marcell Bán)
'''

import business
from business import connect_to_db


@connect_to_db
def first_task():
    cursor = business.cursor
    query = "SELECT first_name, last_name FROM mentors;"
    cursor.execute(query)
    results = cursor.fetchall()
    return {
        'title': 'First task',
        'text': 'First and last names of all the mentors',
        'headers': [
            'First name', 'Last name'
        ],
        'table': results
    }


@connect_to_db
def second_task():
    cursor = business.cursor
    query = "SELECT nick_name FROM mentors WHERE city='Miskolc';"
    cursor.execute(query)
    results = cursor.fetchall()
    return {
        'title': 'Second task',
        'text': 'Nicknames of the mentors located at Miskolc',
        'headers': [
            'Nickname'
        ],
        'table': results
    }


@connect_to_db
def third_task():
    cursor = business.cursor
    query = "SELECT (first_name || ' ' || last_name) AS full_name, phone_number "
    query += "FROM applicants WHERE first_name='Carol';"
    cursor.execute(query)
    results = cursor.fetchall()
    return {
        'title': 'Third task',
        'text': 'Full name and phone number of Carol',
        'headers': [
            'Full name', 'Phone number'
        ],
        'table': results
    }


@connect_to_db
def fourth_task():
    cursor = business.cursor
    query = "SELECT (first_name || ' ' || last_name) AS full_name, phone_number "
    query += "FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';"
    cursor.execute(query)
    results = cursor.fetchall()
    return {
        'title': 'Fourth task',
        'text': 'Full name and phone number of the other girl',
        'headers': [
            'Full name', 'Phone number'
        ],
        'table': results
    }


@connect_to_db
def fifth_task():
    cursor = business.cursor
    query = "SELECT * FROM applicants WHERE application_code=54823;"
    cursor.execute(query)
    results = cursor.fetchall()
    if len(results) == 0:
        query = "INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) "
        query += "VALUES (%s, %s, %s, %s, %s);"
        data = ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823)
        cursor.execute(query, data)
        query = "SELECT * FROM applicants WHERE application_code=54823;"
        cursor.execute(query)
        results = cursor.fetchall()
    return {
        'title': 'Fifth task',
        'text': 'Inserted the new applicant below',
        'headers': [
            'ID', 'First name', 'Last name', 'Phone number', 'Email', 'Application code'
        ],
        'table': results
    }


@connect_to_db
def sixth_task():
    cursor = business.cursor
    query = "UPDATE applicants SET phone_number=%s WHERE first_name='Jemima' AND last_name='Foreman';"
    cursor.execute(query, ('003670/223-7459',))
    query = "SELECT first_name, last_name, phone_number FROM applicants "
    query += "WHERE first_name='Jemima' AND last_name='Foreman';"
    cursor.execute(query)
    results = cursor.fetchall()
    return {
        'title': 'Sixth task',
        'text': 'Changed Jemima Foreman\'s phone number',
        'headers': [
            'First name', 'Last name', 'Phone number'
        ],
        'table': results
    }


@connect_to_db
def seventh_task():
    cursor = business.cursor
    query = "DELETE FROM applicants_mentors WHERE applicant_id IN "
    query += "(SELECT id FROM applicants WHERE email LIKE '%@mauriseu.net');"
    cursor.execute(query)
    query = "DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';"
    cursor.execute(query)
    return {
        'title': 'Seventh task',
        'text': 'Deleted the applicants with the domain "mauriseu.net"'
    }

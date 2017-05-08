'''
display and input functions for the SI7 SQL assignment
by night5word (Marcell Bán)
'''

import sys
from terminaltables import SingleTable

SEP_CHAR = '='
SEP_WIDTH = 50


def display_menu(menu_items):
    menu_counter = 1
    for item in menu_items:
        print('{}) {}'.format(menu_counter, item))
        menu_counter += 1
    print('0) Exit')


def get_input(message):
    return input(message)


def display_results_table(pretable_text, headers, results):
    print(pretable_text)
    results.insert(0, headers)
    print(SingleTable(results).table)
    print(get_separator())


def display_message(message):
    print(message)
    print(get_separator())


def display_error(error):
    print(error, file=sys.stderr)


def get_separator():
    return SEP_CHAR * SEP_WIDTH

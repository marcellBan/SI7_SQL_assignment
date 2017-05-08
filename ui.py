'''
display and input functions for the SI7 SQL assignment
by night5word (Marcell Bán)
'''

from terminaltables import SingleTable


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

'''
display and input functions for the SI7 SQL assignment
by night5word (Marcell Bán)
'''


def display_menu(menu_items):
    menu_counter = 1
    for item in menu_items:
        print('{}. {}'.format(menu_counter, item))
        menu_counter += 1
    print('0. Exit')


def get_input(message):
    return input(message)

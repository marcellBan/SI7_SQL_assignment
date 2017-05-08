'''
main module for the SI7 SQL assignment
by night5word (Marcell Bán)
'''

import os
import ui
import business

MENU_ITEMS = (
    'First task',
    'Second task',
    'Third task',
    'Fourth task',
    'Fifth task',
    'Sixth task',
    'Seventh task'
)


def main():
    # get connection data from the environment
    connection_data = {
        'dbname': os.environ.get('MY_PSQL_DBNAME'),
        'user': os.environ.get('MY_PSQL_USER'),
        'host': os.environ.get('MY_PSQL_HOST'),
        'password': os.environ.get('MY_PSQL_PASSWORD')
    }
    db_cursor = business.connect_to_db(connection_data)
    if db_cursor is not None:
        # generates the list of valid selection options
        # (numbers from 0 to 7 in str form)
        valid_selections = [str(x) for x in range(len(MENU_ITEMS) + 1)]
        running = True
        while running:
            ui.display_menu(MENU_ITEMS)
            selection = None
            while selection not in valid_selections:
                selection = ui.get_input('Please select a menu item: ')
            if selection == '0':
                running = False
            else:
                try:
                    business.TASKS[selection](db_cursor)
                except Exception as e:
                    ui.display_error(e)
    else:
        print('Sorry something went wrong while connecting to the database.')

if __name__ == '__main__':
    main()

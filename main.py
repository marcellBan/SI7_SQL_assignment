'''
main module for the SI7 SQL assignment
by night5word (Marcell Bán)
'''

import os
import ui
import business


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
        valid_selections = [str(x) for x in range(8)]
        running = True
        while running:
            ui.display_menu()
            selection = None
            while selection not in valid_selections:
                selection = ui.get_input('Please select a menu item: ')
            if selection == '0':
                running = False
            elif selection == '1':
                business.first_task(db_cursor)
            elif selection == '2':
                business.second_task(db_cursor)
            elif selection == '3':
                business.third_task(db_cursor)
            elif selection == '4':
                business.fourth_task(db_cursor)
            elif selection == '5':
                business.fifth_task(db_cursor)
            elif selection == '6':
                business.sixth_task(db_cursor)
            elif selection == '7':
                business.seventh_task(db_cursor)
    else:
        print('Sorry something went wrong while connecting to the database.')

if __name__ == '__main__':
    main()

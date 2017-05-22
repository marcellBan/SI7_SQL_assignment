'''
main module for the SI7 SQL assignment
by night5word (Marcell Bán)
'''

from flask import Flask, render_template
from constants import MENU_ITEMS, OLD_TASKS
import business

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', menu=MENU_ITEMS)


@app.route('/old/<int:num>')
def old_tasks(num):
    return render_template('display_results.html', data=OLD_TASKS[num - 1]())


@app.route('/mentors')
def mentors_and_schools():
    return render_template('display_results.html', data=business.mentors_and_schools())


@app.errorhandler(500)
def internal_error(error_message):
    return render_template('500.html', message=error_message), 500

if __name__ == '__main__':
    app.run()

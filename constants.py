import old_business

OLD_TASKS = [
    old_business.first_task,
    old_business.second_task,
    old_business.third_task,
    old_business.fourth_task,
    old_business.fifth_task,
    old_business.sixth_task,
    old_business.seventh_task
]

MENU_ITEMS = {
    'old_tasks': (
        ('First task', '/old/1'),
        ('Second task', '/old/2'),
        ('Third task', '/old/3'),
        ('Fourth task', '/old/4'),
        ('Fifth task', '/old/5'),
        ('Sixth task', '/old/6'),
        ('Seventh task', '/old/7')
    ),
    'new_tasks': (
        ('Mentors and schools', '/mentors'),
        ('All schools', '/all-school'),
        ('Mentors by country', '/mentors-by-country'),
        ('Contacts', '/contacts'),
        ('Applicants', '/applicants'),
        ('Applicants and mentors', '/applicants-and-mentors')
    )
}

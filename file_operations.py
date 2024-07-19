import os, fnmatch

def create_to_do_txt():
    if not os.path.isfile('To_do_list.txt'):
        with open('To_do_list.txt', 'w') as todo_txt:
            pass

def add_task_to_txt(id, task, desc, start_date, deadline):
    with open('To_do_list.txt', 'w') as todo_txt:
        todo_txt.write(f'{id}, {task}, {desc}, {start_date}, {deadline}\n')
import os, fnmatch, random, todo_class
from datetime import datetime


#Creating .txt file to keep all task together
def create_to_do_txt():
    if not os.path.isfile('To_do_list.txt'):
        with open('To_do_list.txt', 'w') as todo_txt:
            pass

#Adding task to the .txt file
def add_task_to_txt():
    with open('To_do_list.txt', 'a+') as todo_txt:
        for task_details in todo_class.List.template.keys():
            #Separating by | between details because on first thought commonly used comma (,) to do so, can be also used during description of tasks and it's
            #getting harder to clearly read it and split in other part of the code
            #todo_txt.write(f"{input(f'{task_details}: '.title())} | ")
            todo_txt.write(f"{random.randint(1,10)} | ")
        todo_txt.write('\n')

#Importing task list from .txt file
def import_task_list_txt(main_todo_list):
    with open('To_do_list.txt', 'r') as todo_txt:
        tasks_number = todo_txt.readlines()

        #Setting file pointer on start was needed cause of .readlines() method usage which placed pointer at the end of the file
        todo_txt.seek(0)
        imported_txt = todo_txt.read()
        imported_tasks = [value.strip() for value in imported_txt.split("|") if value.strip()]

        for task_number in range(len(tasks_number)):
            new_task = todo_class.List.template.copy()
            current_task = imported_tasks[len(new_task)*task_number : len(new_task)*(task_number+1)]
            for key, detail in zip(new_task.keys(), current_task):
                new_task[f'{key}'] = detail
            main_todo_list.add_task(new_task)

def export_task_list_txt(main_todo_list):
    with open('To_do_list.txt', 'w') as todo_txt:
        tasks_number = len(main_todo_list.get_list())
        todo_txt.write(str(tasks_number))





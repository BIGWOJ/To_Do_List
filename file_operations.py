import os, fnmatch, random, todo_class
from datetime import datetime

#Adding task to the .txt file
def add_task_to_txt(new_task=None):
    with open('To_do_list.txt', 'a+') as todo_txt:
        if new_task:
            for task_detail in new_task.values():
                todo_txt.write(f'{str(task_detail)} | ')
            todo_txt.write('\n')

        else:
            for task_details in todo_class.List.template.keys():
                #Separating by | between details because on first thought commonly used comma (,) to do so, can be also used during description of tasks and it's
                #getting harder to clearly read it and split in other part of the code
                #todo_txt.write(f"{input(f'{task_details}: '.title())} | ")
                todo_txt.write(f'{random.randint(1,10)} | ')
            todo_txt.write('\n')

#Importing task list from the .txt file
def import_task_list_txt(main_todo_list):
    #Try to open .txt file
    try:
        with open('To_do_list.txt', 'r') as todo_txt:
            tasks_number = todo_txt.readlines()

            #Setting file pointer back on start was needed cause of .readlines() method usage which placed pointer at the end of the file
            todo_txt.seek(0)
            imported_txt = todo_txt.read()
            imported_tasks = [value.strip() for value in imported_txt.split("|") if value.strip()]

            for task_number in range(len(tasks_number)):
                new_task = todo_class.List.template.copy()
                #Task details read by read() method return concatenated list of all values from dictionary of task
                #Hence values separation of each task was needed based on length (numbers) of keys in it
                current_task = imported_tasks[len(new_task)*task_number : len(new_task)*(task_number+1)]
                for key, detail in zip(new_task.keys(), current_task):
                    new_task[f'{key}'] = detail
                main_todo_list.add_task(new_task, imported_task=True)
    #If opening .txt file was unsuccessful -> continue application
    except FileNotFoundError:
        pass

#Może się przyda?
def sort_task_list_txt(main_todo_list):
    import_task_list_txt(main_todo_list)
    pass

def update_txt(main_task_list):
    with open('To_do_list.txt', 'w+') as todo_txt:
        #Number of tasks in current list
        list_tasks_number = len(main_task_list.get_list())
        #Number of tasks in .txt file
        txt_tasks_number = len(todo_txt.readlines())
        #Rewriting .txt file to update tasks in it
        if list_tasks_number != txt_tasks_number:
            for task in main_task_list.get_list():
                for task_detail in todo_class.List.template.keys():
                    # print(task)
                    # print(task_detail[])
                    todo_txt.write(f'{str(task[task_detail])} | ')
                todo_txt.write('\n')

def erase_tasks(main_todo_list):
    with open('To_do_list.txt', 'w') as todo_txt:
        pass


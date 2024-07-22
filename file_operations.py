import os, fnmatch, random
from datetime import datetime

#Creating .txt file to keep all task together
def create_to_do_txt():
    if not os.path.isfile('To_do_list.txt'):
        with open('To_do_list.txt', 'w') as todo_txt:
            pass

#Adding task to the .txt file
def add_task_to_txt():
    with open('To_do_list.txt', 'r+') as todo_txt:
        id = random.randint(1,10)
        task = input("Enter task name: ")
        desc = input("Describe your task (optional): ")
        start_date_input = input("Enter start date in DD.MM.YYYY format (optional): ")
        deadline_input = input("Enter deadline in DD.MM.YYYY format (optional): ")
        priority = input('Priority:\n'
                         'ASAP -> 1\n'
                         'High -> 2\n'
                         'Medium -> 3\n'
                         'WIthin couple days -> 4\n'
                         'Chill -> 5\n')
        try:
            start_date = datetime.strptime(start_date_input, "%d.%m.%Y")
            deadline = datetime.strptime(deadline_input, "%d.%m.%Y")
        except ValueError:
            print("Wrong date format!")

        #Getting number of lines in .txt files which is equivalent to number of tasks
        id = len(todo_txt.readlines()) + 1
        todo_txt.write(f'{id}, {task}, {desc}, {start_date.strftime("%d.%m.%Y")}, {deadline.strftime("%d.%m.%Y")}, {priority}\n')

#Deleting given chosen
def delete_task(task_id):
    with open('To_do_list.txt', 'r+') as todo_txt:
        lines = todo_txt.readlines()
        task_counter = 0
        #Searching for line (task) with matching task_id
        for line in lines:
            if line[0].split(',')[0] == str(task_id):
                lines.pop(task_counter)
            task_counter += 1
        #Setting .txt pointer at the beginning
        todo_txt.seek(0)
        todo_txt.writelines(lines)
        #Shorten file if needed
        todo_txt.truncate()
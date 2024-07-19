import file_operations
import random
import time
from datetime import datetime

task_template = {'id': '',
                'task': '',
                'description': '',
                'start_date': '',
                'deadline': ''}

task_list = []

#print('podaj deadline zadania: ')
date = datetime.today().strftime("%d.%m.%Y")
day = int(date[:2])
month = int(date[3:5])
year = int(date[-4:])

# date1 = datetime(year, month, day)
# date2 = datetime(1939, 10, 25)
# # print(date1-date2)
# for i in range(3):
#     new_task = task_template.copy()
#     for task_details in new_task.keys():
        #task[f'{task_details}'] = input(f'{task_details.title()}: ')
        #new_task[f'{task_details}'] = random.randint(1,10)

    #task_list.append(new_task)


file_operations.create_to_do_txt()
l = random.randint(1,10)
file_operations.add_task_to_txt(l,l,l,l,l)


# print(task_list)
# print(task_list[0])
# print(task_list[1])
# print(task_list[2])

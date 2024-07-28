import file_operations
import random
import time
from datetime import datetime
import todo_class

todo_list = todo_class.List()
#todo_list.create_list()

# todo_list.add_task()
# todo_list.add_task()
# for task in todo_list.get_list():
#     print(task)
#
#
# todo_list.delete_task(2)
# print('po:\n')
#
# print('\nprzed:')
# for task in todo_list.get_list():
#     print(task)
#
file_operations.add_task_to_txt()
file_operations.add_task_to_txt()
file_operations.import_task_list_txt(todo_list)
#
# print('\npo:')
# for task in todo_list.get_list():
#     print(task)
#
# todo_list.add_task()
#
# print('\npo2:')
# for task in todo_list.get_list():
#     print(task)

print(len(todo_list.get_list()))
file_operations.export_task_list_txt(todo_list)
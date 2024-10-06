import file_operations
from datetime import datetime

class List:
    def __init__(self, task_list):
        self.task_list = task_list

    #Task template
    template = {'id': '',
                'task': '',
                'description': '',
                'start_date': '',
                'deadline': '',
                'priority': ''}

    #Getting list of tasks
    def get_list(self):
        return self.task_list

    #Deleting task list / getting new one
    def delete_list(self):
        self.task_list = []

    #Adding task to the list
    def add_task(self, new_task, imported_task=False):
        self.task_list.append(new_task)

        #If task was imported from .txt file there is no need to write it again to the file - handling double writing to the file
        if not imported_task:
            file_operations.add_task_to_txt(new_task)

    #Deleting task based on ID
    def delete_task(self, task_id):
        tasks_numbers = task_id.split(',')
        self.task_list = [task for task in self.task_list if task['id'] not in tasks_numbers]

    #Sorting function based on different conditions
    def sort_list(self, condition='priority'):
        match condition:
            case 'priority':
                self.task_list.sort(key=lambda x: int(x['priority']))
            case 'start_date':
                self.task_list.sort(key=lambda x: datetime.strptime(x['start_date'], '%d.%m.%Y'))
            case 'deadline':
                self.task_list.sort(key=lambda x: datetime.strptime(x['deadline'], '%d.%m.%Y'))

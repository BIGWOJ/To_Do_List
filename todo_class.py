import file_operations
from datetime import datetime
import random

class List:
    def __init__(self):
        self.tasks = []

    #Task template
    template = {'id': '',
                'task': '',
                'description': '',
                'start_date': '',
                'deadline': '',
                'priority': ''}

    def create_list(self):
        self.tasks = []

    #Getting list of tasks
    def get_list(self):
        return self.tasks

    #Adding task to the list
    def add_task(self, imported_task=None):
        new_task = List.template.copy()
        for task_details in new_task.keys():
            if imported_task:
                new_task = imported_task
                #self.tasks.append(imported_task)
            else:
                #print('a')
                if task_details in ['start_date', 'deadline']:
                    day = random.randint(1, 28)  # Dla uproszczenia, aby uniknąć niepoprawnych dat
                    month = random.randint(1, 12)
                    year = 2024
                    date = f'{day:02}.{month:02}.{year}'
                    new_task[f'{task_details}'] = str(date)
                    continue

                new_task[f'{task_details}'] = random.randint(1, 50)
                #new_task[f'{task_details}'] = input(f'{task_details}: '.title())
        self.tasks.append(new_task)
        if not imported_task:
            file_operations.add_task_to_txt(new_task)

    #Deleting task based on id
    def delete_task(self, id):
        self.tasks = [task for task in self.tasks if task['id'] != str(id)]

    def sort(self, condition='priority'):
        match condition:
            case 'priority':
                return self.tasks.sort(key=lambda x: int(x['priority']))
            case 'start_date':
                return self.tasks.sort(key=lambda x: datetime.strptime(x['start_date'], '%d.%m.%Y'))
            case 'deadline':
                return self.tasks.sort(key=lambda x: datetime.strptime(x['deadline'], '%d.%m.%Y'))

        # def f(a):
        #     return int(a['id'])
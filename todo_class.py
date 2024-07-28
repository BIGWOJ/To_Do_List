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
                new_task[f'{task_details}'] = random.randint(1, 10)
                #new_task[f'{task_details}'] = input(f'{task_details}: '.title())
        self.tasks.append(new_task)

    #Deleting task based on id
    def delete_task(self, id):
        self.tasks = [task for task in self.tasks if task['id'] != str(id)]


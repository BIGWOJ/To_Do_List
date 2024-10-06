import file_operations, todo_class
import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog, QMessageBox, QFileDialog, QLabel, QApplication, QDialog, QRadioButton

class SelectionWindow(QDialog):
    def __init__(self, parent=None):
        #UI for selecting sorting condition window
        super().__init__(parent)
        self.setWindowTitle('Sorting condition')

        layout = QVBoxLayout()
        self.options = ['priority', 'start_date', 'deadline']
        self.option_1 = QRadioButton("Priority")
        self.option_2 = QRadioButton("Start date")
        self.option_3 = QRadioButton("Deadline")
        layout.addWidget(self.option_1)
        layout.addWidget(self.option_2)
        layout.addWidget(self.option_3)

        self.select_button = QPushButton('Select')
        self.select_button.clicked.connect(self.accept)
        layout.addWidget(self.select_button)
        self.setLayout(layout)

    #Returning tuple True/False representing which option was selected
    def option_selected(self):
        return self.option_1.isChecked(),self.option_2.isChecked(),self.option_3.isChecked()

class GUI_buttons(QWidget):
    standard_font_size = 16
    def __init__(self, main_task_list):
        super().__init__()
        self.buttons()
        self.main_task_list = main_task_list
        file_operations.import_task_list_txt(self.main_task_list)

    #Creating UI buttons and connecting them with functions
    def buttons(self):
        #Setting connections of buttons
        self.add_task_button = QPushButton("Add task", self)
        self.add_task_button.clicked.connect(self.add_task)

        self.delete_tasks_button = QPushButton("Delete tasks", self)
        self.delete_tasks_button.clicked.connect(self.delete_tasks)

        self.show_tasks_button = QPushButton("Show tasks", self)
        self.show_tasks_button.clicked.connect(self.show_tasks)

        self.sort_tasks_button = QPushButton("Sort tasks", self)
        self.sort_tasks_button.clicked.connect(self.sort_tasks)

        self.exit_app_button = QPushButton("Exit application", self)
        self.exit_app_button.clicked.connect(self.exit_app)

        #Setting UI
        layout = QVBoxLayout(self)
        layout.addWidget(self.add_task_button)
        layout.addWidget(self.delete_tasks_button)
        layout.addWidget(self.show_tasks_button)
        layout.addWidget(self.sort_tasks_button)
        layout.addWidget(self.exit_app_button)

        self.setLayout(layout)
        self.resize(250,250)
        self.setWindowTitle("TDL v1.0")

#Adding new task
    def add_task(self):
        window = QWidget()
        window_layout = QVBoxLayout(window)
        window.setStyleSheet(f'font: {GUI_buttons.standard_font_size}px')

        #Creating task template copy to be able to fill it with new details without changing template
        new_task = todo_class.List.template.copy()

        for task_detail in todo_class.List.template.keys():
            if task_detail == 'id':
                #Adding 1 to secure ID starting from 0, not 1
                new_task[f'{task_detail}'] = len(self.main_task_list.get_list())+1
            else:
                new_task[f'{task_detail}'] = QInputDialog.getText(window, "", f"{task_detail.title().replace('_',' ')}:")[0]

        #Adding created task to the list
        self.main_task_list.add_task(new_task)

#Showing all tasks
    def show_tasks(self):
        #Checking if there is any task in the list, if not -> import tasks from .txt file
        if len(self.main_task_list.get_list()) == 0:
           file_operations.import_task_list_txt(self.main_task_list)

        #If still there is no task (in .txt file wasn't any task as well) -> pop-up message
        if len(self.main_task_list.get_list()) == 0:
            QMessageBox.information(None, "", "You have no tasks to do!")

        #Otherwise (there is any task) -> listing them
        else:
            tasks_details_list = []
            for index, task in enumerate(self.main_task_list.get_list()):
                if index == 0:
                    font_color = 'rgb(255, 50, 10)'
                elif index == 1:
                    font_color = 'rgb(200, 50, 10)'
                elif index == 2:
                    font_color = 'rgb(175, 50, 10)'
                else:
                    font_color = 'lightgray'
                #Creating n
                task_details = " ".join([f"{key.title().replace('_', ' ')}: {task[key]}" for key in todo_class.List.template.keys()])
                tasks_details_list.append(f"<p style='color: {font_color};'>{task_details}</p>")
                task_details_html = "<p>".join(tasks_details_list)
            QMessageBox.information(QWidget(), '', f'{task_details_html}')

    #Sorting tasks based on given condition
    def sort_tasks(self):
        sorting_conditions = SelectionWindow()
        sorting_conditions.exec()
        #Getting sorting condition by searching index from tuple where is True
        #True value means this condition option was selected via UI
        sorting_condition_index = sorting_conditions.option_selected().index(True)
        sorting_condition = sorting_conditions.options[sorting_condition_index]
        todo_class.List.sort_list(self.main_task_list, condition=sorting_condition)
        #Updating .txt file after sorting
        file_operations.update_txt(self.main_task_list)

    #Deleting tasks
    def delete_tasks(self):
        window = QWidget()
        window_layout = QVBoxLayout(window)
        window.setStyleSheet(f'font: {GUI_buttons.standard_font_size}px')
        #Getting task_id of task wanted to be deleted
        task_id = QInputDialog.getText(window, '', f"Enter task ID:\n**Separated with comma with few IDs**\n'all' to delete all tasks")[0]
        current_tasks_number = len(self.main_task_list.get_list())

        #Using .lower() to secure all variants of writing word 'all', like 'All', 'aLl' etc...
        if task_id.lower() == 'all':
            file_operations.delete_all_tasks(self.main_task_list)
            QMessageBox.information(QWidget(), '', 'All tasks deleted successfully')

        else:
            todo_class.List.delete_task(self.main_task_list, task_id)
            #This if statement means task was/were deleted
            if current_tasks_number != len(self.main_task_list.get_list()):
                if current_tasks_number - len(self.main_task_list.get_list()) != 1:
                    QMessageBox.information(QWidget(), '', f'Tasks IDs: {task_id} deleted successfully')
                else:
                    QMessageBox.information(QWidget(), '', f'Task ID: {task_id} deleted successfully')
                file_operations.update_txt(self.main_task_list)
            #Otherwise - task wasn't deleted
            else:
                QMessageBox.information(QWidget(), '', f"Task ID: {task_id} wasn't found")

#Function to exit application
    def exit_app(self):
        exit(0)

def app_exec(main_task_list):
    app = QApplication(sys.argv)
    #Manually checked the RGB color of logo background
    logo_background_color = (40, 40, 40)

    #QPushButton like "OK", "Cancel" buttons
    #GUI_buttons QPushButton - exit app
    app.setStyleSheet(f"""
        QWidget {{
            font: {GUI_buttons.standard_font_size}px;
            color: lightgray;
            background-color: rgb({logo_background_color[0]}, {logo_background_color[1]}, {logo_background_color[2]})
        }}
        
        QMessageBox {{
            font: {GUI_buttons.standard_font_size}px;
            color: lightgray;
            background-color: rgb({logo_background_color[0]}, {logo_background_color[1]}, {logo_background_color[2]})
        }}

        QPushButton {{
            font: {GUI_buttons.standard_font_size}px;
            color: black;
            background-color: lightgray
        }}

        GUI_buttons QPushButton {{
            font: bold 22px;
            color: rgb({logo_background_color[0]}, {logo_background_color[1]}, {logo_background_color[2]});
            border-width: 2px;
            border-style: solid;
            border-color: black;
            background-color: lightgray
        }}
        """)

    main_window = GUI_buttons(main_task_list)
    main_window.show()
    app.exec_()
import file_operations, todo_class
import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog, QMessageBox, QFileDialog, QLabel, QApplication

class GUI_buttons(QWidget):
    standard_font_size = 16
    def __init__(self, main_task_list):
        super().__init__()
        self.buttons()
        self.main_task_list = main_task_list

    #Creating UI buttons and connecting them with functions
    def buttons(self):
        self.add_task_button = QPushButton("Add task", self)
        self.add_task_button.clicked.connect(self.add_task)

        self.show_tasks_button = QPushButton("Show tasks", self)
        self.show_tasks_button.clicked.connect(self.show_tasks)

        self.exit_app_button = QPushButton("Exit application", self)
        self.exit_app_button.clicked.connect(self.exit_app)

        layout = QVBoxLayout(self)
        layout.addWidget(self.add_task_button)
        layout.addWidget(self.show_tasks_button)
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
            new_task[f'{task_detail}'] = QInputDialog.getText(window, "", f"{task_detail.title().replace('_',' ')}:")[0]

        #Adding created task to the list
        self.main_task_list.add_task(new_task)

#Showing all tasks
    def show_tasks(self):
        window = QWidget()
        window_layout = QVBoxLayout(window)
        window.setStyleSheet(f'font: {GUI_buttons.standard_font_size}px')

        #Checking if there is any task in the list, if not -> import tasks from .txt file
        if len(self.main_task_list.get_list()) == 0:
            file_operations.import_task_list_txt(self.main_task_list)

        #If still there is no task (in .txt file wasn't any task as well) -> pop-up message
        if len(self.main_task_list.get_list()) == 0:
            QMessageBox.information(None, " ", "You have no tasks to do!")

        #Otherwise (there are any task) -> listing them
        else:
            task_details = "\n\n".join([f"ID: {task['id']}, Task: {task['task']}, Description: {task['description']}, "
                                        f"Start date: {task['start_date']}, Deadline: {task['deadline']}, Priority: {task['priority']}" for task in self.main_task_list.get_list()])
            QMessageBox.information(QWidget(), '', f'{task_details}')

#Function to exit application
    def exit_app(self):
        exit(0)

def app_exec(main_task_list):
    app = QApplication(sys.argv)
    # Manually checked the RGB color of logo background
    logo_background_color = (40, 40, 40)

    # QPushButton like "OK" "Cancel"
    # GUI_buttons QPushButton - import file and exit app
    app.setStyleSheet(f"""
        QWidget {{
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
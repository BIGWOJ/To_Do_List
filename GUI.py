import file_operations, todo_class
import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog, QMessageBox, QFileDialog, QLabel, QApplication
class GUI_buttons(QWidget):
    standard_font_size = 16
    def __init__(self):
        super().__init__()
        self.buttons()

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

    def add_task(self):
        #print('asd')
        window = QWidget()
        window_layout = QVBoxLayout(window)
        window.setStyleSheet(f'font: {GUI_buttons.standard_font_size}px')
        price, _ = QInputDialog.getDouble(window, " ",
                                          f"\nEnter the price of:", decimals=2)
        # for task_detail in todo_class.List.template.keys():
        #     #new_task[f'{task_detail}'] = QInputDialog(window, f'{task_detail}'.title())
        #     a,_ = QInputDialog.getDouble(window, f'{task_detail}'.title())
        #     print(a)

        #todo_class.List.add_task()
        # return

    def show_tasks(self):
        pass

    def exit_app(self):
        exit(0)


def app_exec():
    app = QApplication(sys.argv)
    # Manually checked the RGB color of logo background
    logo_background_color = (37, 37, 37)

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

    main_window = GUI_buttons()
    main_window.show()
    app.exec_()
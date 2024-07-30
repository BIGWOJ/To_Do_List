import todo_class, GUI

##################
#####
##### W show_tasks() zrobić tak, żeby pierwsze 3 zadania miały kolory -> 1. czerwony, drugi mniej czerwony, trzeci najmniej ->
##### żeby wiedzieć, które jest najważniejsze do zrobienia
#####
##### W show_tasks() spróbować zrobić to przy pomocy wypisywania klucz i ich wartości a nie ręcznie task['id'] itd
#####
#####
##################

if __name__ == "__main__":
    #Creating todo_list to work with it
    main_todo_list = todo_class.List([])
    GUI.app_exec(main_todo_list)

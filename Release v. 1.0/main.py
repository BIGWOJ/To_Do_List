import todo_class, GUI

if __name__ == "__main__":
    #Creating todo_list to work with it
    main_todo_list = todo_class.List([])
    GUI.app_exec(main_todo_list)

import todo_class, GUI

##################
#####
##### show_tasks() działa jak chciałem, ale jeszcze zrozumieć i okomentować dobrze ten kod -> dużo z html jest
#####
##### dokończyć delete_task()
#####
##################

if __name__ == "__main__":
    #Creating todo_list to work with it
    main_todo_list = todo_class.List([])
    GUI.app_exec(main_todo_list)

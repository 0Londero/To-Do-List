# Imports
from feature_view import view
from feature_add import add_task
from feature_delete import delete_tasks

# Global Variable
tasks = []

# Application Loop
while True:

    print(r"""
████████  ██████        ██████   ██████      ██      ██ ███████ ████████
   ██    ██    ██       ██   ██ ██    ██     ██      ██ ██         ██
   ██    ██    ██ █████ ██   ██ ██    ██     ██      ██ ███████    ██
   ██    ██    ██       ██   ██ ██    ██     ██      ██      ██    ██
   ██     ██████        ██████   ██████      ███████ ██ ███████    ██
            By: Otávio Londero, Maria Zamora, Yuan Chang.
    """)

    while True:


        print("""
        #########  To-Do List  #########
        1. Add Task
        2. Remove Task
        3. View Tasks / Suggest Tasks
        4. Exit
        """)

        user_choice = int(input("Your Choice:   "))
        if user_choice == 1:
            add_task(tasks)
        elif user_choice == 2:
            delete_tasks(tasks)
        elif user_choice == 3:
            view(tasks)
        elif user_choice == 4:
            break
    break
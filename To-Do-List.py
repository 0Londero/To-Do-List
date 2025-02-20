# Imports
from feature_view import view
from feature_add import add_task
from feature_delete import delete_tasks
from feature_menu import display_menu

# Global Variable
tasks = []

# Art
print(r"""
████████  ██████        ██████   ██████      ██      ██ ███████ ████████
   ██    ██    ██       ██   ██ ██    ██     ██      ██ ██         ██
   ██    ██    ██ █████ ██   ██ ██    ██     ██      ██ ███████    ██
   ██    ██    ██       ██   ██ ██    ██     ██      ██      ██    ██
   ██     ██████        ██████   ██████      ███████ ██ ███████    ██
            By: Otávio Londero, Maria Zamora, Yuan Chang.
    """)

# Application Loop
while True:

    display_menu()

    # Choice verification
    while True:
        user_choice = input("Your Choice:   ")
        if user_choice in ['1', '2', '3', '4']:
            break  # Valid choice, exit verification loop
        print("Invalid choice! Please, try again.")

    # Main choices
    if user_choice == '1':
        add_task(tasks)
    elif user_choice == '2':
        delete_tasks(tasks)
    elif user_choice == '3':
        view(tasks)
    elif user_choice == '4':
        break  # Exit the program
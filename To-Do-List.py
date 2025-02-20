# Imports
from feature_view import view


# Initializing a global variable for saving the Task
from logging import exception

task = []

#Define add new list
import datetime
def add_task():

#Task
    while True:
        new_task = input("Enter the task : ")
        if new_task == " ":
            print("\033[31mTask can't be empty\033[0m")
            continue
        else:
            break

#Priority
    while True:
        priority = input("Enter the priority (1 = high, 2 = medium, 3 = low) : ")
        if priority not in ["1", "2", "3"] :
            print("\033[31mInvalid priority. Please enter 1, 2, or 3\033[0m")
            continue
        else:
            break

#Date
    while True:
        date = input("Enter the deadline (YYYY-MM-DD) : ")
        try:
            deadline = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            today = datetime.date.today()
            if deadline < today :
                print("\033[31mThe deadline can't be past date.\033[0m")
                continue
            else:
                break

        except ValueError:
            print("\033[31mInvalid deadline. Please enter in YYYY-MM-DD format.\033[0m")
            continue

    task.append({"Task" : new_task, "Priority" : priority, "Deadline" : date})
    print(f'Your task : \033[33m{new_task}\033[0m with priority : \033[33m{priority}\033[0m and deadline : \033[33m{date}\033[0m has been added to the list.')

#Ask process
while True :
    print()
    print("To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice : "))
        if choice == 1 :
            add_task()

        else:
            print("\033[31mInvalid choice. Please enter a number between 1 and 4\033[0m")
    except ValueError:
        print("\033[31mPlease enter a valid number.\033[0m")


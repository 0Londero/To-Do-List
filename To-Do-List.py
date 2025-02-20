"""
Create a simple to-do list application that allows users to add, remove, and view
tasks. This project will help you practice working with lists and functions in
Python.
"""

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


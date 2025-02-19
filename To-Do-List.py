"""
Create a simple to-do list application that allows users to add, remove, and view
tasks. This project will help you practice working with lists and functions in
Python.
"""

# Initializing a global variable for saving the Task
task = []

#example of variables added - temporary information
task.append({"name":"example", "priority": 3,"deadline":'2025-2-15'})
task.append({"name":"example2", "priority": 1,"deadline":'2025-2-17'})
task.append({"name":"example3", "priority": 3,"deadline":'2025-2-27'})
task.append({"name":"example4", "priority": 1,"deadline":'2025-2-20'})
task.append({"name":"example5", "priority": 1,"deadline":'2025-2-22'})
print(len(task))
choice = 4

if choice == 4:
    n = 0
    if len(task) < 10:
        n=len(task)
        suggestion = sorted(task, key=lambda elem:(elem['deadline'],elem['priority']))[:n]
    if len(task)>=10:
        suggestion = sorted(task, key=lambda elem: (elem['deadline'], elem['priority']))[:10]
    
    print("Hi! Here are some tasks you might want to work on: ")
    print(suggestion)

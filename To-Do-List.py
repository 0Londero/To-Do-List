"""
Create a simple to-do list application that allows users to add, remove, and view
tasks. This project will help you practice working with lists and functions in
Python.
"""

# Initializing a global variable for saving the Task
task = []


#example of variables added - temporary information
task.append({"name":"example", "priority": "high","deadline":['2025-2-18']})
task.append({"name":"example2", "priority": "low","deadline":['2025-2-18']})
task.append({"name":"example3", "priority": "low","deadline":['2025-2-18']})
print(task)
choice = 2
#Function to remove the item
def remove_it(indexn):
    task.pop(indexn)
    print("Task " + task_name + " has been removed from the list")

#Validation of the option
if choice == 2:
    task_name = input("Please enter the name of the task to remove:")
    #initial validation
    validation_list = 0
    for index in range(len(task)):
        print(task[index]["name"])
        name_val = task[index]["name"]
        indexn = index
        if task_name == name_val:
            remove_it(indexn)
            validation_list=1
   # when the item is not in the list
    while validation_list==0:
        task_name = input("Sorry the name is not in the list, please enter the name of the task to remove:")
        #Second validation it is in the list
        for index in range(len(task)):
            print(task[index]["name"])
            name_val=task[index]["name"]
            indexn=index
            if task_name == name_val:
                remove_it(indexn)
                validation_list=1
#It is not required the print but just for now
print(task)


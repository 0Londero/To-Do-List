def Delete_Task():
validation=0
if choice == 2:
    task_name = input("Please enter the name of the task to remove:")
    # initial validation
    for index in range(len(task)):
        if validation!=1:
            name_val = task[index]["name"]
            indexn2 = index
            if task_name == name_val:
                ValidationQ = input("Are you sure you want to eliminate " + name_val + " ? (Y/N)")
                while True:
                    if ValidationQ == "Y":
                        task.pop(indexn2)
                        print("Task " + task_name + " has been removed from the list")
                        break
                    if ValidationQ == "N":
                        print("Task " + task_name + " hasn't been removed from the list")
                        break
                    ValidationQ = input(
                        "Are you sure you want to eliminate " + name_val + " ? Please select a valid answer (Y/N)")
                validation = 1
    # when the item is not in the list
    while validation!=1:

        task_name = input("Sorry the name is not in the list, please enter the name of the task to remove:")

        # Second validation it is in the list
        for index in range(len(task)):
            if validation!=1:
                name_val = task[index]["name"]
                indexn2 = int(index)
                if task_name == name_val:
                    ValidationQ = input("Are you sure you want to eliminate " + name_val + " ? (Y/N)")
                    while True:
                        if ValidationQ == "Y":
                            task.pop(indexn2)
                            print("Task " + task_name + " has been removed from the list")
                            break
                        if ValidationQ == "N":
                            print("Task " + task_name + " hasn't been removed from the list")
                            break
                        ValidationQ = input("Are you sure you want to eliminate " + name_val + " ? Please select a valid answer (Y/N)")
                    validation = 1


def delete_tasks(tasks):
    validation = 0
    tasks_name = input("Please enter the name of the tasks to remove:")
    # initial validation
    for index in range(len(tasks)):
        if validation!=1:
            name_val = tasks[index]["Task"]
            indexn2 = index
            if tasks_name == name_val:
                validationq = input("Are you sure you want to eliminate " + name_val + " ? (Y/N)")
                while True:
                    if validationq == "Y" or validationq == "y":
                        tasks.pop(indexn2)
                        print("Task " + tasks_name + " has been removed from the list")
                        break
                    if validationq == "N" or validationq == "n":
                        print("Task " + tasks_name + " hasn't been removed from the list")
                        break
                    validationq = input(
                        "Are you sure you want to eliminate " + name_val + " ? Please select a valid answer (Y/N)")
                validation = 1
    # when the item is not in the list
    while validation!=1:

        tasks_name = input("Sorry the name is not in the list, please enter the name of the tasks to remove:")

        # Second validation it is in the list
        for index in range(len(tasks)):
            if validation!=1:
                name_val = tasks[index]["Task"]
                indexn2 = int(index)
                if tasks_name == name_val:
                    validationq = input("Are you sure you want to eliminate " + name_val + " ? (Y/N)")
                    while True:
                        if validationq == "Y" or validationq == "y":
                            tasks.pop(indexn2)
                            print("Task " + tasks_name + " has been removed from the list")
                            break
                        if validationq == "N" or validationq == "n":
                            print("Task " + tasks_name + " hasn't been removed from the list")
                            break
                        validationq = input("Are you sure you want to eliminate " + name_val + " ? Please select a valid answer (Y/N)")
                    validation = 1
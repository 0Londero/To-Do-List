import datetime
def add_task(tasks):

#Task
    while True:
        new_task = input("Enter the task : ").strip()
        if not new_task :
            print("\033[31mTask can't be empty. Please try again.\033[0m")
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
        date = input("Enter the deadline (YYYY-MM-DD) : ").strip()
        try:
            deadline = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            today = datetime.date.today()
            if deadline < today :
                print("\033[31mThe deadline can't be past date.\033[0m")
                continue
            if len(date) != 10:
                print("\033[31mInvalid deadline. Please enter in YYYY-MM-DD format.(Ex. 2025-05-31)\033[0m")
                continue
            else:
                break

        except ValueError:
            print("\033[31mInvalid deadline. Please enter in YYYY-MM-DD format.(Ex. 2025-05-31)\033[0m")
            continue

    tasks.append({"Task" : new_task, "Priority" : priority, "Deadline" : date})
    print(f'Your task : \033[33m{new_task}\033[0m with priority : \033[33m{priority}\033[0m and deadline : \033[33m{date}\033[0m has been added to the list.')

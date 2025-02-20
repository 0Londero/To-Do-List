def view(tasks):

    sorted_tasks = tasks        # Default
    # Function to return the specific item
    def get_priority(task):
        return task['Priority']
    def get_date(task):
        return task['Deadline']
    def get_suggestion(task):
        return task['Deadline'], task['Priority']
    # If the list is empty
    if not tasks:
        print("Nothing to see here. Try adding some task first :) ")
        return
    # Loop for a valid answer
    while True:
        char = input("Do you want to sort? (Y/N): ").strip().upper()
        if char in ["Y", "N"]:
            break # Valid Choice
        print("Invalid choice! Please, try again.") # Invalid = loop

    if char == "Y": # Yes
        while True:
            char1 = input("Sort by Priority (P), Date (D), or Suggestion (S)? ").strip().upper()

            if char1 == "P":
                sorted_tasks = sorted(tasks, key=get_priority)
                break
            elif char1 == "D":
                sorted_tasks = sorted(tasks, key=get_date)
                break
            elif char1 == "S":
                sorted_tasks = sorted(tasks, key=get_suggestion)
                if len(sorted_tasks) < 10:
                    sorted_tasks = sorted_tasks[:len(sorted_tasks)]  # Keep all if less than 10
                else:
                    sorted_tasks = sorted_tasks[:10]  # Keep only top 10
                break
            else:
                print("Invalid choice! Please, try again.")
    # Print the list if the choice is Valid; # No sort = default list print
    for item in sorted_tasks:
        print(f"Description: {item['Task']} | Priority: {item['Priority']} | Date: {item['Deadline']}")
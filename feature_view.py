def view():

    sorted_tasks = tasks        # Default
    # Function to return the specific item
    def get_priority(task):
        return task['priority']
    def get_date(task):
        return task['date']
    def get_suggestion(task):
        return task['date'], task['priority']
    # If the list is empty
    if not tasks:
        print("Nothing to see here. Go add some task first.")
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
                break
            else:
                print("Invalid choice! Please, try again.")
    # Print the list if the choice is Valid; # No sort = default list print
    for item in sorted_tasks:
        print(f"[{item['id']}] Description: {item['description']} | Priority: {item['priority']} | Date: {item['date'].strftime('%Y-%m-%d')}")
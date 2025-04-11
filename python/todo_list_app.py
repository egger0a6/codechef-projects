from datetime import datetime
def userChoice(choice, tasks):
    if choice == 1:
        task_name = input("Enter task name: ")
        deadline = input("Enter deadline (DD-MM-YYYY): ")
        add_task(tasks, task_name, deadline)
    elif choice == 2:
        # Check if there are any tasks before proceeding
        if not tasks:
            print("No tasks available.\n")
            return
        

        # Display existing tasks before asking for deletion
        display_tasks(tasks)
        

        task_number = int(input("Enter task number to delete: "))
        delete_task(tasks, task_number)
    elif choice == 3:
        display_tasks(tasks) 
    elif choice == 4:
        pass
    elif choice == 5: 
        return ("Exiting application. Goodbye!")
    else:
        print("Invalid choice!\n")

# Update the below Function
def delete_task(tasks, task_number):
    task_index = task_number - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['task']}' deleted successfully!\n")
    else:
        print("Invalid task number!\n")

    # task_idk = task_number - 1
    # if task_idx <= 0 or task_idx >= len(tasks):
    #     print("Invalid task number!\n")
    # else:
    #     removed_task = tasks.pop(task_idx)
    #     print(f"Task '{removed_task["task"]}' deleted successfully!\n")

def validate_date(deadline):
    try:
        deadline_date =  datetime.strptime(deadline, "%d-%m-%Y").date()
        return deadline_date
    except ValueError:
        print("Invalid date format! Try again.\n")
        return None


def add_task(tasks, task_name, deadline):
    deadline_date = validate_date(deadline)
    if deadline_date:
        tasks.append({"task": task_name, "deadline": deadline_date})
        print("Task added successfully!\n")

# TODO ask if user wants to change task, or mark complete
# def update_task(tasks, )




def display_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return
    print("\nYour Tasks:")
    index = 0
    for task in tasks:
        formatted_deadline = task['deadline'].strftime("%d-%m-%Y")  # Display in DD-MM-YYYY format 
        print(f"{index+1}. {task['task']} - Deadline: {formatted_deadline}")
        index += 1
    print()

if __name__ == "__main__":
    # List to store Tasks
    tasks = []
    print("""
Welcome to the To-Do List Application!
    """)
    
    while True:
        print("Choose one operation:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Update Task")
        print("5. Exit")
        print()

        try:
          choice = int(input("Enter your choice: ").strip())
          if 1 <= choice <= 5:
            value  = userChoice(choice, tasks)
            if value == "Exiting application. Goodbye!":
                print(value)
                break
          else:
              print("Error: Invalid number. Please enter a different choice.")
              print()
        except ValueError:
            print("Error: That is not an integer. Please enter a different choice.")
            print()
        
'''
TODO 
use regex to test date

Add an Update Task Feature - Allow users to modify an existing task instead of deleting and re-adding it.

Implement an Exception Handler - Currently, we only validate user choice for integers, but if a user enters a character or an invalid input, the program may crash. Improve error handling to make it more robust.

Mark Tasks as Completed – Instead of deleting, allow users to mark tasks as "Done" and keep a record of completed tasks.
'''        
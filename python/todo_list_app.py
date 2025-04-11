from datetime import datetime

def userChoice(choice, tasks, completed_tasks):
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
        
        task_number = validate_choice("del")
        if task_number:
          delete_task(tasks, task_number)
        else:
            return
    elif choice == 3:
        display_tasks(tasks) 
    elif choice == 4:
        if not tasks:
            print("No tasks available \n")
            return

        update_task(tasks, completed_tasks)
    elif choice == 5:
        display_completed(completed_tasks)
    elif choice == 6: 
        return ("Exiting application. Goodbye!")
    else:
        print("Invalid choice!\n")


def delete_task(tasks, task_number):
    task_idx = task_number - 1
    if task_idx < 0 or task_idx >= len(tasks):
        print("Invalid task number!\n")
    else:
        removed_task = tasks.pop(task_idx)
        print(f"Task '{removed_task["task"]}' deleted successfully!\n")


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


def update_task(tasks, completed_tasks):
    print("Choose one operation:")
    print("1. Update Task")
    print("2. Mark Task Completed")

    choice = validate_choice("choose")
    if choice:
        if choice == 1:
            display_tasks(tasks)
            task_idx = validate_choice("update")
            if task_idx:
                task_idx = task_idx - 1
                if task_idx < 0 or task_idx >= len(tasks):
                  print("Invalid task number!\n")
                else:
                    print("Enter new details or leave blank to leave task/deadline unchanged.")
                    task_name = input("Enter task name: ")
                    deadline = input("Enter deadline (DD-MM-YYYY): ")
                    if task_name: 
                        tasks[task_idx]["task"] = task_name
                    if deadline:
                        deadline_date = validate_date(deadline)
                        if deadline_date:
                          tasks[task_idx]["deadline"] = deadline_date
                    print(f"Task successfully updated!\n")
            else:
                return
        else:
          display_tasks(tasks)
          task_idx = validate_choice("complete")
          if task_idx:
              task_idx = task_idx - 1
              if task_idx < 0 or task_idx >= len(tasks):
                  print("Invalid task number!\n")
              else:
                  completed_task = tasks.pop(task_idx)
                  completed_task["deadline"] = "Complete"
                  completed_tasks.append(completed_task)
                  print(f"Task '{completed_task["task"]}' successfully marked complete!\n")
          else:
              return
    else:
        return


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


def display_completed(tasks):
    if not tasks:
        print("No tasks completed.\n")
        return
    index = 0
    for task in tasks:
        print(f"{index+1}. {task['task']} - Deadline: {task["deadline"]}")
        index += 1
    print()


def validate_choice(type):
    try:
        if type == "choose":
          choice = int(input("Enter your choice: ").strip())
        elif type == "del":
            choice = int(input("Enter your task number to delete: ").strip())
        elif type == "update":
            choice = int(input("Enter your task number to update: ").strip())
        elif type == "complete":
            choice = int(input("Enter task number to mark completed: ").strip())
        if 1 <= choice <= 6:
            return choice
        else:
            print("Error: Invalid number. Please enter a different choice.")
            print()
            return None
    except ValueError:
      print("Error: That is not an integer. Please enter a different choice.")
      print()
      return None


if __name__ == "__main__":
    # List to store Tasks
    tasks = []
    completed_tasks = []
    print("""
Welcome to the To-Do List Application!
    """)
    
    while True:
        print("Choose one operation:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Update Task")
        print("5. Display Completed Tasks")
        print("6. Exit")
        print()

        choice = validate_choice("choose")
        if choice:
          value  = userChoice(choice, tasks, completed_tasks)
          if value == "Exiting application. Goodbye!":
              print(value)
              break
        else:
            continue        
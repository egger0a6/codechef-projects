from datetime import datetime
import re
import os

FILE_NAME = "/home/chef/workspace/students.txt"


def user_choice(choice):
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting Student Database Manager...")
        return
    else:
        print("Invalid choice. Please enter a valid option.")





#--------------------------------------------------------
    

def add_student():
    """Function to add a new student record to the file."""
    

def view_students():
    """Function to display all student records from the file."""
    

def search_student(return_data=False):
    """Function to search for a student by ID or Name."""


def update_student():
    """Function to update an existing student record in the file."""
    

def delete_student():
    """Function to delete a student record from the file."""


if __name__ == '__main__':
    while True:
        print("\n Student Database Manager")
        print("1. Add a Student")
        print("2. View All Students")
        print("3. Search Student by ID or Name")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        user_choice(choice)
        if(choice==6):
            break
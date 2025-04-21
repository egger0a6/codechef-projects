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
    

def add_student():
    student_id = input("Enter Student Roll Number (Numeric): ").strip()
    if not student_id.isdigit():
        print("Invalid Roll Number! It should contain only numbers.")
        return
    
    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.startswith(f"{student_id},"):
                print("Student Roll Number already exists. Use update option instead.")
                return

    name = input("Enter First Name: ").strip()
    if not name.isalpha():
        print("Invalid Name! Name should contain only alphabets.")
        return

    age = input("Enter Age: ").strip()
    if not age.isdigit() or int(age) > 100:
        print("Invalid Age! Age should be a number under 100.")
        return

    course = input("Enter Course: ").strip()
    department = input("Enter Department: ").strip()


    
    with open(FILE_NAME, "a") as file:
        file.write(f"{student_id},{name},{age},{course},{department}\n")

    print("Student added successfully!")
    

def view_students():
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    
    if not lines:
        print("No student records found.")
        return
    
    print("\nStudent Records:")
    print('Roll Number\tName\tAge\tCourse\tDepartment')
    for line in lines:
        student = line.strip().split(",")
        student_id, name, age, course, department = student
        print(student_id,"\t\t",name,"\t",age,"\t",course,"\t",department)
    

def search_student(return_data=False):
    query = input("Enter Student Roll Number or Name to search: ").strip()

    with open(FILE_NAME, "r") as file:
        for line in file:
            student_id, name, age, course, department = line.strip().split(",")
            if query == student_id or query.lower() == name.lower():
                print("\nStudent Found:")
                print('Roll Number\tName\tAge\tCourse\tDepartment')
                print(student_id,"\t\t",name,"\t",age,"\t",course,"\t",department)
                return

    print("Student not found.")


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
# Dictionary to store contacts
contacts = {}

def userChoice(choice):
    """Handles user input and calls the corresponding function."""
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Goodbye!")
        return
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")


def add_contact():
    name = input("Enter contact name: ").strip()
    phone_number = input("Enter phone number (10 digits): ").strip()

    if not name or not phone_number.isdigit() or len(phone_number) != 10:
        print("Invalid input! Please enter a valid name and 10-digit phone number.")
        return

    if phone_number in contacts:
        print("Contact already exists!")
    else:
        contacts[phone_number] = name
        print(f"Contact '{name}' added successfully!")


def view_contacts():
    """Displays all contacts."""
    
def search_contact():
    """Searches for a contact."""
    
def update_contact():
    """Updates a contact."""
    
def delete_contact():
    """Deletes a contact."""


# Main execution loop
if __name__ == '__main__':
    while True:
        print("\n📞 Contact Manager Menu:")
        print("1. Add a Contact")
        print("2. View Contacts")
        print("3. Search for a Contact")
        print("4. Update a Contact")
        print("5. Delete a Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        userChoice(choice)
        if(choice==6):
            break
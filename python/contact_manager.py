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
    if not contacts:
        print("No contacts available!")
        return
    
    print("Contact List: ")
    for phone, contact in contacts.items():
        print(f"{contact}: {phone}")


def search_contact():
    query = input("Enter name or phone number to search: ").strip()

    if query in contacts:
        print(f"{contacts[query]}: {query}")
        return

    found = False
    for phone, name in contacts.items():
        if name.lower() == query.lower():
            print(f"{name}: {phone}")
            found = True

    if not found:
        print("Contact not found!")

    
def update_contact():
    if not contacts:
        print("No contacts available to update!")
        return
    
    phone = input("Enter phone number to update name: ").strip()

    if phone in contacts:
        current_name = contacts[phone]
        new_name = input(f"Current name: {current_name}\nEnter new name: ").strip()

        if new_name:
            contacts[phone] = new_name
            print(f"Successfully updated name to: {new_name} ({phone})")
        else:
            print("Name cannot be empty!")
            return
    else:
        print(f"Contact with phone '{phone}' not found!")
        return
    
def delete_contact():
    if not contacts:
        print("No contacts available to delete!")
        return

    name_to_delete = input("Enter name of contact to delete: ").strip()

    phone_to_delete = None
    for phone, name in contacts.items():
        if name.lower() == name_to_delete.lower():
            phone_to_delete = phone
            break
    
    if not phone_to_delete:
        print(f"No contact found with name '{name_to_delete}'")
        return
    
    del contacts[phone_to_delete]
    print(f"Contact '{name_to_delete}' deleted successfully!")


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
import csv

# Inventory dictionary to store products (product_name: [quantity, price])
inventory = {}


def add_product():
    """Adds a new product to the inventory with proper validation."""
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))

    if name in inventory:
        inventory[name][0] += quantity
    else:
        inventory[name] = [quantity, price]

    print(f"Product '{name}' added successfully!\n")


# -------------------------------------------------


def view_inventory():
    # For Viewing Inventory
    print("View")

def update_stock():
    # For Updating Stock
    print("Update")

def delete_product():
    # For Deleting Inventory
    print("Delete")

def search_product():
    # For Searching a Product
    print("Search")

def save_inventory():
    # Saving in inventory
    print("Save")

if __name__ == "__main__":

    while(True):
        print("1. Add Product\n2. View Inventory\n3. Update Stock\n4. Delete Product\n5. Search Product\n6. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            search_product()
        elif choice == "6":
            save_inventory()
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.\n")
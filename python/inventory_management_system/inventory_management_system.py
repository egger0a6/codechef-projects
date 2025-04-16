import csv

# Inventory dictionary to store products (product_name: [quantity, price])
inventory = {}


def add_product():
    """Adds a new product to the inventory with proper validation."""
    name = input("Enter product name: ").strip()
    quantity = int(input("Enter quantity: ").strip())
    price = float(input("Enter price per unit: ").strip())

    if name in inventory:
        inventory[name][0] += quantity
        print(f"Product '{name}' already catalogued. Added quantity: {quantity}. New stock: {inventory[name][0]}")
    else:
        inventory[name] = [quantity, price]
        print(f"Product '{name}' added successfully!\n")


def view_inventory():
    if not inventory:
        print("Inventory is empty! \n")
        return
    
    print("Current Inventory:")
    print("Name\tQuantity\tPrice")
    for name, details in inventory.items():
        print(f"{name}\t{details[0]}\t\t${details[1]:.2f}")
    print()


def update_stock():
    name = input("Enter product name to update: ").strip()

    if name in inventory:
        new_quantity = int(input("Enter new quantity: ").strip())
        inventory[name][0] = new_quantity
        print(f"Updated '{name}' stock to {new_quantity}\n")
    else:
        print("Product not found!\n") 


def delete_product():
    name = input("Enter product name to delete: ").strip()

    if name in inventory:
        del inventory[name]
        print(f"Deleted '{name}' from inventory\n")
    else:
        print("Product not found!\n")


def search_product():
    name = input("Enter Product name to search: ")

    if name in inventory:
        print(f"{name}: Quantity={inventory[name][0]}, Price=${inventory[name][1]:.2f}\n")
        return
    else:
        print("Product not found!")


def save_inventory():
    # Saving in inventory
    print("Save")


if __name__ == "__main__":
    while(True):
        print("1. Add Product\n2. View Inventory\n3. Update Stock\n4. Delete Product\n5. Search Product\n6. Save & Exit")
        choice = input("Enter your choice: ").strip()

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
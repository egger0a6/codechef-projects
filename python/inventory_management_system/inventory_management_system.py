import csv

# Inventory dictionary to store products (product_name: [quantity, price])
inventory = {}


def add_product():
    #TODO update to allow category
    """Adds a new product to the inventory with proper validation."""
    name = input("Enter product name: ").strip()
    category = input("Enter product category").strip()
    quantity = int(input("Enter quantity: ").strip())
    price = float(input("Enter price per unit: ").strip())

    if name in inventory:
        inventory[name][0] += quantity
        print(f"Product '{name}' already catalogued. Added quantity: {quantity}. New stock: {inventory[name][0]}")
    else:
        inventory[name] = [quantity, price, category]
        print(f"Product '{name}' added successfully!\n")


def view_inventory():
# TODO update to show category and format output better
    if not inventory:
        print("Inventory is empty! \n")
        return
    
    print("Current Inventory:")
    print("Name\tQuantity\tPrice")
    for name, details in inventory.items():
        print(f"{name}\t{details[0]}\t\t${details[1]:.2f}")
    print()


def update_stock():
    # TODO allow user to update name, category, and price
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
# TODO update to save category
    try:
        with open("inventory.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Quantity", "Price"])
            for name, details in inventory.items():
                writer.writerow([name, details[0], details[1]])
            print("Inventory saved to 'inventory.csv'\n")
    except Exception as e:
        print(f"An error occurred while saving the inventory: {e}\n")


def load_inventory():
# TODO update to load category
    try:
        with open("inventory.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) == 3:
                    name = row[0]
                    quantity = int(row[1])
                    price = float(row[2])
                    inventory[name] = [quantity, price]
            print("Inventory loaded successfully.")
    except FileNotFoundError:
        print("inventory.csv not found. Starting with an empty inventory.")
    except Exception as e:
        print(f"An error occurred while loading the inventory: {e}")


def sort_inventory():
    # TODO allow user to sort by name, category, price, or quantity
    pass


def alert_low_stock():
    min_stock = 3
    low_stock_alerts = []

    for product in inventory:
        if inventory[product][0] <= min_stock:
            low_stock_alerts.append(f"Alert: '{product}' inventory is low!")
    
    if low_stock_alerts:
        print("-"*40)
        for alert in low_stock_alerts:
            print(alert)
        print("-"*40)

def clear_inventory():
    # TODO allow user to wipe inventory
    pass


if __name__ == "__main__":
    # TODO add options to sort and clear
    load_inventory()
    while(True):
        alert_low_stock()
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
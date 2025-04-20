import sys
import csv
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QMessageBox, 
    QTableWidget, QTableWidgetItem, QInputDialog, QHeaderView, QGridLayout
)
from PyQt5.QtGui import QScreen

""" 
    Instruct Qt framework to use the X11 display server backend instead of
    Wayland on Ubuntu 24.04. This is necessary because the default display
    server backend on this version, Wayland, prevents apps from setting 
    their absolute positioning on top level windows. Use for testing purposes.
"""
# import os
# # Force X11 backend
# os.environ["QT_QPA_PLATFORM"] = "xcb"

inventory = {}

class InventoryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Manager")
        self.setGeometry(100, 100, 800, 700)
        self.center_window()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.init_ui()
        self.load_inventory()
        self.display_inventory()

    def center_window(self):
        screen = QApplication.primaryScreen()
        screen_rect = self.frameGeometry()
        screen_center = screen.availableGeometry().center()
        screen_rect.moveCenter(screen_center)
        self.move(screen_rect.topLeft())

    def init_ui(self):
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Product Name")

        self.quantity_input = QLineEdit(self)
        self.quantity_input.setPlaceholderText("Quantity")

        self.price_input = QLineEdit(self)
        self.price_input.setPlaceholderText("Price")

        self.category_input = QLineEdit(self)
        self.category_input.setPlaceholderText("Category")

        button_layout = QGridLayout()

        buttons = [
            ("Add Product", self.add_product),
            ("Update Product", self.update_stock),
            ("Delete Product", self.delete_product),
            ("Sort Inventory", self.sort_inventory),
            ("Search Product", self.search_product),
            ("Save Inventory", self.save_inventory),
            ("Wipe Inventory", self.clear_inventory)
        ]

        for i, (label, func) in enumerate(buttons):
            btn = QPushButton(label, self)
            btn.clicked.connect(func)
            
            # Special styling for "Wipe Inventory"
            if label == "Wipe Inventory":
                btn.setStyleSheet("""
                    QPushButton {
                        border: 2px solid #ff0f0f;
                        border-radius: 2px;
                        padding: 5px 15px;
                    }
                    QPushButton:hover {
                        background-color: #ffc2c2;
                    }
                    QPushButton:pressed {
                        background-color: #ff0f0f;
                    }
                """)
            
            row = i // 2
            col = i % 2
            button_layout.addWidget(btn, row, col)

        refresh_button = QPushButton("Refresh Table", self)
        refresh_button.clicked.connect(self.display_inventory)

        self.table = QTableWidget()
        self.table.setSortingEnabled(True)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Product Name", "Quantity", "Price", "Category"])
        header = self.table.horizontalHeader()
        for i in range(self.table.columnCount()):
            if i == 0:
                header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
        else:
            header.setSectionResizeMode(i, QHeaderView.Stretch)

        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.quantity_input)
        self.layout.addWidget(self.price_input)
        self.layout.addWidget(self.category_input)
        self.layout.addLayout(button_layout)
        self.layout.addWidget(self.table)
        self.layout.addWidget(refresh_button)


    def display_inventory(self):
        low_stock_quantity = 3

        self.table.setRowCount(0)
        for i, (name, details) in enumerate(inventory.items()):
            self.table.insertRow(i)
            if details[0] <= low_stock_quantity:
                name += f" (⚠️ Low stock!)"
            self.table.setItem(i, 0, QTableWidgetItem(name))
            self.table.setItem(i, 1, QTableWidgetItem(str(details[0])))
            self.table.setItem(i, 2, QTableWidgetItem(f"${details[1]:.2f}"))
            self.table.setItem(i, 3, QTableWidgetItem(details[2]))

    def add_product(self):
        name = self.name_input.text().strip()

        if not name:
          QMessageBox.warning(self, "Input Error", "Product name cannot be empty.")
          return
        
        quantity = self.quantity_input.text().strip()
        price = self.price_input.text().strip()
        category = self.category_input.text().strip()

        if quantity:
            try:
                quantity = int(quantity)
            except ValueError:
                QMessageBox.warning(self, "Input Error", "Please enter a valid numeric value for quantity.")
                return
        else:
            quantity = 0

        if price:
            try:
                price = float(price)
            except ValueError:
                QMessageBox.warning(self, "Input Error", "Please enter a valid numeric value for price.")
                return
        else:
            price = 0.0
            
        if quantity < 0 or price < 0:
            QMessageBox.warning(self, "Input Error", "Quantity and Price cannot be negative.")
            return
        
        if name in inventory:
            inventory[name][0] += quantity
        else:
            inventory[name] = [quantity, price, category]

        self.clear_inputs()
        self.display_inventory()

    def update_stock(self):
        name = self.name_input.text().strip()
        if name not in inventory:
            QMessageBox.warning(self, "Error", "Product not found!")
            return

        new_name, ok_name = QInputDialog.getText(self, "New Name", "Enter new name (leave blank to keep unchanged):")
        new_quantity, ok_quantity = QInputDialog.getInt(self, "New Quantity", "Enter new quantity (leave 0 to keep unchanged):", 0)
        new_price, ok_price = QInputDialog.getDouble(self, "New Price", "Enter new price (leave 0 to keep unchanged):", 0.0, decimals=2)
        new_category, ok_cat = QInputDialog.getText(self, "New Category", "Enter new category (leave blank to keep unchanged):")

        current_quantity, current_price, current_category = inventory[name]

        updated_name = new_name if new_name else name
        updated_quantity = new_quantity if new_quantity else current_quantity
        updated_price = new_price if new_price else current_price
        updated_category = new_category if new_category else current_category

        del inventory[name]
        inventory[updated_name] = [updated_quantity, updated_price, updated_category]

        self.clear_inputs()
        self.display_inventory()

    def delete_product(self):
        name = self.name_input.text().strip()
        if name in inventory:
            reply = QMessageBox.question(
                self, 
                "Delete Product?", 
                f"Are you sure you want to delete {name}?", 
                QMessageBox.Yes | QMessageBox.No, 
                QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                del inventory[name]
                self.display_inventory()
            else:
                return
        else:
            QMessageBox.warning(self, "Error", "Product not found!")

    def search_product(self):
        query = self.name_input.text().strip().lower()
        self.table.setRowCount(0)
        for name, details in inventory.items():
            if query in name.lower():
                row = self.table.rowCount()
                self.table.insertRow(row)
                self.table.setItem(row, 0, QTableWidgetItem(name))
                self.table.setItem(row, 1, QTableWidgetItem(str(details[0])))
                self.table.setItem(row, 2, QTableWidgetItem(f"${details[1]:.2f}"))
                self.table.setItem(row, 3, QTableWidgetItem(details[2]))

    def sort_inventory(self):
        options = ["Name", "Quantity", "Price", "Category"]
        choice, ok = QInputDialog.getItem(self, "Sort Inventory", "Choose sort method:", options, editable=False)
        if not ok:
            return

        if choice == "Name":
            sorted_items = sorted(inventory.items(), key=lambda x: x[0])
        elif choice == "Quantity":
            sorted_items = sorted(inventory.items(), key=lambda x: x[1][0])
        elif choice == "Price":
            sorted_items = sorted(inventory.items(), key=lambda x: x[1][1])
        elif choice == "Category":
            sorted_items = sorted(inventory.items(), key=lambda x: x[1][2])
        else:
            return

        inventory.clear()
        inventory.update(sorted_items)
        self.display_inventory()

    def clear_inputs(self):
        self.name_input.clear()
        self.quantity_input.clear()
        self.price_input.clear()
        self.category_input.clear()

    def save_inventory(self):
        try:
            with open("inventory.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Product Name", "Quantity", "Price", "Category"])
                for name, details in inventory.items():
                    writer.writerow([name, details[0], details[1], details[2]])
        except Exception as e:
            QMessageBox.critical(None, "Save Error", f"An error occurred while saving: {e}")

    def load_inventory(self):
        try:
            with open("inventory.csv", "r", newline="") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if len(row) == 4:
                        name = row[0]
                        quantity = int(row[1])
                        price = float(row[2])
                        category = row[3]
                        inventory[name] = [quantity, price, category]
        except FileNotFoundError:
            pass
        except Exception as e:
            QMessageBox.critical(None, "Load Error", f"An error occurred while loading: {e}")

    def clear_inventory(self):
        reply = QMessageBox.question(
            self, 
            "Wipe Inventory?", 
            "This cannot be undone! Continue?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            inventory.clear()
            QMessageBox.information("Inventory wiped successfully!")
            

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 
            "Confirm Exit", 
            "Are you sure you want to quit? Inventory will be saved.", 
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.save_inventory()
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec_())
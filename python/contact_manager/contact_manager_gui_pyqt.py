import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit,
    QListWidget, QMessageBox, QHBoxLayout, QFileDialog
)

class ContactManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📇 Contact Manager")
        self.contacts = {}
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # display area
        self.contact_list = QListWidget()
        layout.addWidget(self.contact_list)

        # input fields
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter contact name")
        layout.addWidget(self.name_input)

        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter 10-digit phone number")
        layout.addWidget(self.phone_input)

        # buttons
        button_layout = QHBoxLayout()
        add_btn = QPushButton("Add Contact")
        view_btn = QPushButton("View Contacts")
        search_btn = QPushButton("Search")
        update_btn = QPushButton("Update Contact")
        delete_btn = QPushButton("Delete Contact")
        save_btn = QPushButton("Save Contacts")
        load_btn = QPushButton("Load Contacts")

        for btn in [add_btn, view_btn, search_btn, update_btn, delete_btn, save_btn, load_btn]:
            button_layout.addWidget(btn)

        layout.addLayout(button_layout)

        # connect buttons
        add_btn.clicked.connect(self.add_contact)
        view_btn.clicked.connect(self.view_contacts)
        search_btn.clicked.connect(self.search_contact)
        update_btn.clicked.connect(self.update_contact)
        delete_btn.clicked.connect(self.delete_contact)
        save_btn.clicked.connect(self.save_contacts_to_json)
        load_btn.clicked.connect(self.load_contacts)

        self.setLayout(layout)

    def show_message(self, title, text):
        QMessageBox.information(self, title, text)

    def add_contact(self):
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()

        if not name or not phone.isdigit() or len(phone) != 10:
            self.show_message("Error", "Enter a valid name and 10-digit number.")
            return

        if phone in self.contacts:
            self.show_message("Exists", "Contact already exists!")
        else:
            self.contacts[phone] = name
            self.show_message("Success", f"Added {name}: {phone}")
            self.view_contacts()

    def view_contacts(self):
        self.contact_list.clear()
        if not self.contacts:
            self.contact_list.addItem("No contacts available.")
        else:
            for phone, name in self.contacts.items():
                self.contact_list.addItem(f"{name}: {phone}")

    def search_contact(self):
        name_query = self.name_input.text().strip()
        phone_query = self.phone_input.text().strip()
        self.contact_list.clear()
        found = False
        for phone, name in self.contacts.items():
            print(phone, name)
            if phone_query == phone or name_query.lower() == name.lower():
                print("Here")
                self.contact_list.addItem(f"{name}: {phone}")
                found = True
        if not found:
            self.contact_list.addItem("Contact not found.")

    def update_contact(self):
        phone = self.phone_input.text().strip()
        new_name = self.name_input.text().strip()

        if phone in self.contacts:
            self.contacts[phone] = new_name
            self.show_message("Updated", f"Updated name for {phone} to {new_name}")
            self.view_contacts()
        else:
            self.show_message("Not Found", f"No contact with phone {phone}.")

    def delete_contact(self):
        name_to_delete = self.name_input.text().strip()
        phone_to_delete = None
        for phone, name in self.contacts.items():
            if name.lower() == name_to_delete.lower():
                phone_to_delete = phone
                break
        if phone_to_delete:
            del self.contacts[phone_to_delete]
            self.show_message("Deleted", f"Deleted {name_to_delete}")
            self.view_contacts()
        else:
            self.show_message("Not Found", f"No contact named {name_to_delete}")

    def save_contacts_to_json(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Contacts", "", "JSON Files (*.json)")
        if file_name:
            try:
                with open(file_name, "w") as f:
                    json.dump(self.contacts, f, indent=4)
                self.show_message("Saved", f"Contacts saved to {file_name}")
            except Exception as e:
                self.show_message("Error", str(e))

    def load_contacts(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Load Contacts", "", "JSON Files (*.json)")
        if file_name and os.path.exists(file_name):
            try:
                with open(file_name, "r") as f:
                    self.contacts = json.load(f)
                self.show_message("Loaded", "Contacts loaded successfully!")
                self.view_contacts()
            except Exception as e:
                self.show_message("Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactManager()
    window.resize(500, 400)
    window.show()
    sys.exit(app.exec_())
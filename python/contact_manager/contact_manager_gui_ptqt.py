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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactManager()
    window.resize(500, 400)
    window.show()
    sys.exit(app.exec_())
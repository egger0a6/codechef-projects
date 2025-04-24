import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QFileDialog, QLabel, QMessageBox
)
from cryptography.fernet import Fernet


class FileEncryptor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Encryption Tool")
        self.setFixedSize(300, 250)

        layout = QVBoxLayout()

        self.label = QLabel("Choose an Action:")
        layout.addWidget(self.label)

        self.generate_btn = QPushButton("Generate Secret Key")
        self.generate_btn.clicked.connect(self.generate_key)
        layout.addWidget(self.generate_btn)

        self.encrypt_btn = QPushButton("Encrypt File")
        self.encrypt_btn.clicked.connect(self.encrypt_file)
        layout.addWidget(self.encrypt_btn)

        self.decrypt_btn = QPushButton("Decrypt File")
        self.decrypt_btn.clicked.connect(self.decrypt_file)
        layout.addWidget(self.decrypt_btn)

        self.setLayout(layout)


    def generate_key(self):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        QMessageBox.information(self, "Success", "Secret Key saved to 'secret.key'.")
    

    def encrypt_file(self):
        input_path, _ = QFileDialog.getOpenFileName(self, "Select File to Encrypt")
        if not input_path:
            return
        output_path, _ = QFileDialog.getSaveFileName(self, "Save Encrypted File")
        if not output_path:
            return
        
        try:
            with open("secret.key", "rb") as key_file:
                key = key_file.read()

            cipher = Fernet(key)

            with open(input_path, "rb") as file:
                original_data = file.read()

            encrypted_data = cipher.encrypt(original_data)

            with open(output_path, "wb") as file:
                file.write(encrypted_data)

            QMessageBox.information(self, "Success", "File encrypted successfully.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Encryption failed:\n{e}")
    
    def decrypt_file(self):
        input_path, _ = QFileDialog.getOpenFileName(self, "Select File to Decrypt")
        if not input_path:
            return
        output_path, _ = QFileDialog.getSaveFileName(self, "Save Decrypted File")
        if not output_path:
            return
        original_path, _ = QFileDialog.getOpenFileName(self, "Select Original File for Verification (Optional)")

        try:
            with open("secret.key", "rb") as key_file:
                key = key_file.read()

                cipher = Fernet(key)

            with open(input_path, "rb") as file:
                encrypted_data = file.read()

            decrypted_data = cipher.decrypt(encrypted_data)

            with open(output_path, "wb") as file:
                file.write(decrypted_data)

            if original_path:
                with open(original_path, "rb") as original_file:
                    original_data = original_file.read()
                if original_data == decrypted_data:
                    QMessageBox.information(self, "Verified", "Decrypted file matches the original!")
                else:
                    QMessageBox.warning(self, "Mismatch", "Decrypted file does NOT match the original!")
            else:
                QMessageBox.information(self, "Success", "File decrypted successfully.")
                    
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Decryption failed:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileEncryptor()
    window.show()
    sys.exit(app.exec_())
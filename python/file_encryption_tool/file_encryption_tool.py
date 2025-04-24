from cryptography.fernet import Fernet

def userChoice(choice):

    if choice == 1:
        generate_key()

    elif choice == 2:
        input_file = input("Enter the file to encrypt: ").strip()
        output_file = input("Enter the output file name: ").strip()
        encrypt_file(input_file, output_file)

    elif choice == 3:
        input_file = input("Enter the file to decrypt: ").strip()
        output_file = input("Enter the output file name: ").strip()
        decrypt_file(input_file, output_file)

    elif choice == 4:
        return "Exiting application... Goodbye!"

    else:
        print("Invalid choice!\n")


def generate_key():
    secret_key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(secret_key)

    print("Key generated and saved in 'secret.key' file. Keep it safe!")


def encrypt_file(input_file, output_file):
    try: 
        with open("secret.key", "rb") as key_file:
            key = key_file.readline().strip()

        cipher = Fernet(key)

        with open(input_file, "rb") as file:
            file_data = file.read()
        
        encrypted_data = cipher.encrypt(file_data)

        with open(output_file, "wb") as file:
            file.write(encrypted_data)

        print("File encrypted successfully!")
    except:
        print("An unexpected error occurred.")

def decrypt_file(input_file, output_file):
    try:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()

        cipher = Fernet(key)

        with open(input_file, "rb") as file:
            encrypted_data = file.read()
        
        decrypted_data = cipher.decrypt(encrypted_data)

        with open(output_file, "wb") as file:
            file.write(decrypted_data)
        
        print("File decrypted successfully!")
    except:
        print("An unexpected error occurred")


if __name__ == "__main__":
    print("Welcome to the File Encryption Tool!")

    while True:
        print("\nChoose one operation:")
        print("1. Generate Key")
        print("2. Encrypt a File")
        print("3. Decrypt a File")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        value = userChoice(choice)
        if value == "Exiting application... Goodbye!":
            print(value)
            break
import random
import string

# Global strings to be used to randomly generate password components
string_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_num = '0123456789'
string_special = '~!@#$%^&*()'


def userInput():
    length = int(input("Enter the length of the password: "))
    use_special_chars = input("Include special characters?(yes/no):").lower() == 'yes'
    use_numbers = input("Include numbers?(yes/no): ").lower() == 'yes'
    return(length, use_special_chars, use_numbers)
    

def generate_password(length, use_special_chars, use_numbers):
    """Generates a random password based on user preferences."""


if __name__ == '__main__':
    length, use_special_chars, use_numbers = userInput()
    generated_password = generate_password(length, use_special_chars, use_numbers)
    print("\nGenerated Password:", generated_password)
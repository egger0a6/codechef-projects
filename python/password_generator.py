import random
import string

# Global strings to be used to randomly generate password components
string_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_num = '0123456789'
string_special = '~!@#$%^&*()'

existing_usernames = []


def userInput():
    length = int(input("Enter the length of the password: "))
    use_special_chars = input("Include special characters?(yes/no):").lower() == 'yes'
    use_numbers = input("Include numbers?(yes/no): ").lower() == 'yes'
    email = input("Enter email address or leave empty to skip: ")
    return(length, use_special_chars, use_numbers, email)
    

def generate_password(length, use_special_chars, use_numbers):
    """Generates a random password based on user preferences."""
    password = ''

    # Generate remaining characters
    password = "".join(random.choice(string_char) for _ in range(length - 2))

    # Replace second last character with number if required
    if use_numbers:
        password += random.choice(string_num)
    else:
        password += random.choice(string_char)

    # Replace last character with special character if required
    if use_special_chars:
        password += random.choice(string_special)
    else:
        password += random.choice(string_char)

    return password


def generate_strong_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation


    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    if length < 2:
        raise ValueError("Password length must be at least 2 to guarantee a digit and special character.")
    
    base_password = "".join(random.choice(all_characters) for _ in range(length - 2))

    digit = random.choice(digits)
    special_char = random.choice(special_characters)

    password = list(base_password + digit + special_char)
    random.shuffle(password)
    password = "".join(password)

    has_digit = any(char in digits for char in password)
    has_special = any(char in special_characters for char in password)

    if has_digit and has_special:
        return password
    else:
        raise ValueError("Password must have one digit and one special character.")

def suggest_username(email):
    base_username = email.split("@")[0]
    username =  base_username

    if username not in existing_usernames:
        return username
    
    for i in range(1, 101):
        variation_type = random.randint(1, 3)
        if variation_type == 1:
            new_username = base_username + str(random.randint(0, 99))
        elif variation_type == 2:
            new_username = base_username + random.choice("._-")
        else:
            new_username = base_username + str(random.randint(0, 99)) + random.choice("._-")
        
        if new_username not in existing_usernames:
            return new_username
    
    return None


if __name__ == '__main__':
    length, use_special_chars, use_numbers, email = userInput()
    generated_password = generate_password(length, use_special_chars, use_numbers)
    strong_password = generate_strong_password(length)
    if email:
        username_suggestion = suggest_username(email)
    print("\nGenerated Password:", generated_password)
    print(f"\nStrong Password: {strong_password}")
    if username_suggestion:
        print(f"Suggested username: {username_suggestion}")
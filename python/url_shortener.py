import hashlib

data = {}  # In-memory dictionary


def user_choice(choice):
    """Handles user input and calls the corresponding function."""
    if choice == "1":
        shorten_url()
    elif choice == "2":
        retrieve_url()
    elif choice == "3":
        print("Exiting... Goodbye!")
    else:
        print("Invalid choice! Try again.")

        
def generate_short_url(long_url):
    """Generating short URL."""
  
def shorten_url():
    """shortening the URL."""
    
def retrieve_url():
    """retrieving original URL."""

if __name__ == "__main__":
    while True:
        print("\nURL Shortener")
        print("1. Shorten a URL")
        print("2. Retrieve Original URL")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()
        user_choice(choice)
        if choice == "3":
            break
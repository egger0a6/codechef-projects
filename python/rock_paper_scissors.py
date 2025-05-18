import random

you_score = 0
computer_score = 0

# Update the get_user_choice() function
def get_user_choice():
    """
    Function to get user's choice (rock, paper, or scissors)
    """
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")


"""
Main code
"""
if __name__ == '__main__':
    print("Let's play Rock, Paper, Scissors!")
    print("This game is the best of 3!")
    print("\n")
    
    n = 0
    while n < 3:
        print(f"Round: {n+1}")
        user_choice = get_user_choice()
        n = n + 1

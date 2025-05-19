import random

you_score = 0
computer_score = 0


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

def get_computer_choice():
    """
    Function to randomly generate computer's choice
    """
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """
    Function to determine the winner of the game
    """
    global you_score, computer_score

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "rock"):
        computer_score += 1
        return "Computer wins this round!"
    else:
        you_score += 1
        return "Congratulations! You win this round!"
    
def overall_winner(you_score, computer_score):
    if you_score < computer_score:
        return("Computer won the overall match")
    elif you_score > computer_score:
        return("You won the overall match")
    else:
        return("The match is a tie")


if __name__ == '__main__':
    print("Let's play Rock, Paper, Scissors!")
    print("This game is the best of 3!")
    print("\n")
    n = int(input("How many rounds do you want to play? "))
    
    while n > 0:
        print(f"Round: {n}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        n = n - 1
        
    print("\n")
    print(overall_winner(you_score, computer_score))

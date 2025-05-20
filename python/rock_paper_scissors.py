import random

you_score = 0
computer_score = 0
round_winners = []


def get_user_choice():
    """
    Function to get user's choice (rock, paper, or scissors)

    * New option: 'water'
    * Water beats paper and scissors. Rock beats water.

    """
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors, or water): ").strip().lower()
        if user_choice in ["rock", "paper", "scissors", "water"]:
            return user_choice
        else:
            print("Invalid choice! Please enter 'rock', 'paper', 'scissors', or 'water'.")

def get_computer_choice():
    """
    Function to randomly generate computer's choice
    """
    return random.choice(['rock', 'paper', 'scissors', 'water'])

def determine_winner(user_choice, computer_choice):
    """
    Function to determine the winner of the game
    """
    global you_score, computer_score

    if user_choice == computer_choice:
        round_winners.append("t")
        return "It's a tie!"
    
    # Rock beats scissors and water
    if user_choice == "rock":
        if computer_choice in ["scissors", "water"]:
            you_score += 1
            round_winners.append(True)
            return "Congratulations! You win this round!"
        else:
            computer_score += 1
            round_winners.append(False)
            return "Computer wins this round!"

    # Paper beats rock
    elif user_choice == "paper":
        if computer_choice == "rock":
            you_score += 1
            round_winners.append(True)
            return "Congratulations! You win this round!"
        elif computer_choice in ["scissors", "water"]:
            computer_score += 1
            round_winners.append(False)
            return "Computer wins this round!"

    # Scissors beats paper
    elif user_choice == "scissors":
        if computer_choice == "paper":
            you_score += 1
            round_winners.append(True)
            return "Congratulations! You win this round!"
        elif computer_choice in ["rock", "water"]:
            computer_score += 1
            round_winners.append(False)
            return "Computer wins this round!"

    # Water beats paper and scissors
    elif user_choice == "water":
        if computer_choice in ["paper", "scissors"]:
            you_score += 1
            round_winners.append(True)
            return "Congratulations! You win this round!"
        elif computer_choice == "rock":
            computer_score += 1
            round_winners.append(False)
            return "Computer wins this round!"
    
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
    
    print(round_winners)
    print("\n")
    for i in range(1, len(round_winners) + 1):
        if round_winners[i-1] == "t":
            print(f"Round {i}: Tie")
        else:
          print(f"Round {i}: {"You" if round_winners[i-1] else "Computer"}")
    print(overall_winner(you_score, computer_score))

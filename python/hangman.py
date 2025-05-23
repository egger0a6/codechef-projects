import time
import random

def choose_word():
    words = [ 'code', 'programming', 'learning', 'practice', 'contests', 'rating']
    return random.choice(words)


def wordDisplay(word, guesses):
    display_word = ""
    for char in word:
        if char in guesses:
            display_word += char + ' '
        else:
            display_word += "_ "

    display_word.strip()
    return display_word


def winningCondition(updated_word, turns):
    if "_" not in updated_word:
        return 1
    elif turns == 0:
        return 0
    else:
        return 2
    

def get_starting_consonants(word):
    shuffled_word = random.sample(word, len(word))
    vowels = "aeiou"
    consonants = ""
    for char in shuffled_word:
        if char not in vowels:
            consonants += char
        if len(consonants) == 2:
            break
    return consonants


if __name__ == '__main__':
    name = input("What is your name? ")
    print("Hello, " + name + ", time to play hangman!")
    time.sleep(1)
    print("Start guessing...\n")
    time.sleep(0.5)
    
    word = choose_word()
    guesses = get_starting_consonants(word)
    turns = len(word) - len(guesses)  # number of turns = length of the word to be guessed
    
    while turns > 0:
        print("\nYou have", turns, 'guesses remaining')
        print(wordDisplay(word, guesses), end=" ")
        print(f"Guesses: {guesses}")
        guess = input("\nguess a character: ").lower()
        
        if guess in guesses:
            print("\nYou have already tried this letter")
            continue
        elif len(guess) > 1 or not guess.isalpha():
            print("\nInvalid guess.")
            continue
        else:
            guesses += guess
    
        if guess not in word:
            turns -= 1
            print("\nWrong, Try again")
        
        updated_word = wordDisplay(word, guesses)
        flag = winningCondition(updated_word, turns)
        
        if flag == 0:
            print("\nYou Lose")
            print("The word was", word)
        elif flag == 1:
            print("\nYou won!")
            print(f"You guessed '{word}' correctly")
            break
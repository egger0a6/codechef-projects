import time
import random

def choose_word():
    words = [ 'code', 'programming', 'learning', 'practice', 'contests', 'rating']
    return random.choice(words)
    

if __name__ == '__main__':
    name = input("What is your name? ")
    print("Hello, " + name + ", time to play hangman!")
    
    word = choose_word()
    print("Word selected for this round is '" + word + "'")
import time
import sys


def userChoice(choice):
    if choice == "1":
        digital_clock()
    elif choice == "2":
        seconds = int(input("Enter the number of seconds to countdown: "))
        countdown_timer(seconds)
    else:
        print("Invalid choice!")


def digital_clock():
    """Displays a digital clock."""

def countdown_timer(seconds):
    """Counts down from a given number of seconds."""

if __name__ == '__main__':
    while True:
        choice = input("Choose an option (1:Digital Clock, 2:Countdown Timer): ")
        userChoice(choice)
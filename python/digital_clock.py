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
    while True:
        curr_time = time.localtime()
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", curr_time)
        print(f"\rCurrent Time: {time_str}", end="", flush=True)
        time.sleep(1)

def countdown_timer(seconds):
    print("Countdown Timer started!")
    while seconds > 0:
        print(f"\rTime remaining: {str(seconds)} seconds", end="")
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")

if __name__ == '__main__':
    while True:
        choice = input("Choose an option (1:Digital Clock, 2:Countdown Timer): ")
        userChoice(choice)
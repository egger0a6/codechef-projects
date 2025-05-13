import time
import threading
import sys

stop_loop = False

def userChoice(choice):
    if choice == "1":
        digital_clock()
    elif choice == "2":
        seconds = int(input("Enter the number of seconds to countdown: "))
        countdown_timer(seconds)
    elif choice == "3":
        return "exit"
    else:
        print("Invalid choice!")

def listen_for_quit():
    global stop_loop
    while True:
        user_input = input()
        if user_input.lower() == "q":
            stop_loop = True
            break

def digital_clock():
    listener_thread = threading.Thread(target=listen_for_quit, daemon=True)
    listener_thread.start()

    while not stop_loop:
        curr_time = time.localtime()
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", curr_time)
        print(f"\rCurrent Time: {time_str}", end="", flush=True)
        time.sleep(1)

    print("\nExited clock display.")

def countdown_timer(seconds):
    print("Countdown Timer started!")
    while seconds > 0:
        print(f"\rTime remaining: {str(seconds)} seconds", end="")
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")
    return

if __name__ == '__main__':
    while True:
        choice = input("Choose an option:\n\n1. Digital Clock\n2. Countdown Timer\n3. Exit program\n")
        choice = userChoice(choice)
        if choice == "exit":
            print("Exiting.")
            break
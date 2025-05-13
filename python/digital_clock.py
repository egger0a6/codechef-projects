import time
import threading
import os
import sys

# ANSI Color Codes for the rainbow
colors = [
    '\033[91m',  # Red
    '\033[92m',  # Green
    '\033[93m',  # Yellow
    '\033[94m',  # Blue
    '\033[95m',  # Magenta
    '\033[96m',  # Cyan
    '\033[97m',  # White
]

RESET = "\033[0m"

# ASCII Art for digits and colon
digits = {
    '0': [" __ ", "|  |", "|  |", "|__|"],
    '1': ["    ", "   |", "   |", "   |"],
    '2': [" __ ", " __|", "|   ", "|__ "],
    '3': [" __ ", " __|", "   |", " __|"],
    '4': ["    ", "|  |", "|__|", "   |"],
    '5': [" __ ", "|__ ", "   |", " __|"],
    '6': [" __ ", "|   ", "|__ ", "|__|"],
    '7': [" __ ", "   |", "   |", "   |"],
    '8': [" __ ", "|__|", "|  |", "|__|"],
    '9': [" __ ", "|__|", "   |", " __|"],
    ':': ["    ", "  o ", "  o ", "    "],
    ' ': ["    ", "    ", "    ", "    "]
}

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

# Function to clear the terminal screen        
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def digital_clock():
    listener_thread = threading.Thread(target=listen_for_quit, daemon=True)
    listener_thread.start()

    color_index = 0

    while not stop_loop:
        clear_screen()

        curr_time = time.localtime()
        time_str = time.strftime("%H:%M:%S", curr_time)

        # Build ASCII clock with rainbow colors
        lines = ["", "", "", ""]
        for char in time_str:
            digit_lines = digits.get(char, ["   ", "   ", "   ", "   "])
            for i in range(4):
                color = colors[color_index % len(colors)] # Cycle through colors
                lines[i] += f"{color}{digit_lines[i]}{RESET} " # Add color and spacing
            color_index += 1
        
        # Print the rainbow clock with borders
        print("+----------------------------------------+")
        print("|              RAINBOW CLOCK             |")
        print("+----------------------------------------+")
        for line in lines:
            print("|" + line.center(36) + "|")
        print("+----------------------------------------+")
        print("\nPress 'q' + Enter to quit.")

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
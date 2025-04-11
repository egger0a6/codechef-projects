import time
import random

def get_questions():
    # Return a list of dictionaries containing quiz questions
    return [
        {
            "question": "Which keyword is used to define a function in Python?", 
            "options": ["A) func", "B) define", "C) def", "D) function"], 
            "answer": "C"
        },
        
        {
            "question": "What is the output of print(2 ** 3) in Python?", 
            "options": ["A) 6", "B) 8", "C) 9", "D) 10"], 
            "answer": "B"
            },

        {
            "question:" "Which of the following operators has the highest precedence?",
            "options:": ["A) % (Modulus)", "B) & (BitWise AND)", "C) ** (Exponent)", "D) > (Comparison)"],
            "answer:": "C"
        },

        {
            "question": "What is the output of the following code:\nvar = \"James Bond\"\nprint(var[2::-1])",
            "options": ["A) Jam", "B) dno", "C) maJ", "D) dnoB semaJ"],
            "answer" : "C"
        },

        {
            "question": "What is the output of the following code:\nvar1 = 1\nvar2 = 2\nvar3 = \"3\"\nprint(var1 + var2 + var3)",
            "options": ["A) 6", "B) 33", "C) 123", "D) TypeError: unsupported operand type(s) for +: 'int' and 'str'"],
            "answer" : "D"
        },

        {
            "question": "What is the output of the following code:\nsampleList = [\"Jon\", \"Kelly\", \"Jessa\"]\nsampleList.append(2, \"Scott\")\nprint(sampleList)",
            "options": ["A) The program executes with an error", "B) ['Jon', 'Kelly', 'Scott', 'Jessa']", "C)  ['Jon', 'Kelly', 'Jessa', 'Scott']", "D) ['Jon', 'Scott', 'Kelly', 'Jessa']"],
            "answer" : "A"
        },

        {
            "question": "What is the output of the following code:\nstr = \"pynative\"\nprint (str[1:3])",
            "options": ["A) py", "B) yn", "C)  pyn", "D) yna"],
            "answer" : "B"
        },

        {
            "question": "What is the output of the following code:\nx = 36 / 4 * (3 +  2) * 4 + 2\nprint (x)",
            "options": ["A) 182.0", "B) 37", "C)  117", "D) The program executes with an error"],
            "answer" : "A"
        },

        {
            "question": "Strings are immutable in Python? When we modify a string (such as concatenation), Python always creates a new String object and assigns the new string to that variable.",
            "options": ["A) True", "B) False"],
            "answer" : "A"
        },

        {
            "question": "What is the output of the following code:\nfor i in range(10, 15, 1):\nprint( i, end=', ')",
            "options": ["A) 10, 11, 12, 13, 14", "B) 10, 11, 12, 13, 14, 15"],
            "answer" : "A"
        },
    ]

def countdown_timer():
    print("\nYou have 10 seconds to think...")
    for i in range(10, 0, -1):
        print(f"\rTime left: {i} seconds ", end="")
        time.sleep(1)
    print("\nTime's up!\n")

def play_quiz():
    print("Welcome to Python Quiz!")
    
    # Get questions
    questions = get_questions()
    
    # Shuffle questions
    random.shuffle(questions)

# --------------------------------------------------   

if __name__ == "__main__":
    play_quiz()
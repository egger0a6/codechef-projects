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
            "question": "Which data type is mutable in Python?", 
            "options": ["A) Tuple", "B) String", "C) List", "D) Integer"], 
            "answer": "C"
        },
        
        {
            "question": "Which of the following is used to take input from the user?", 
            "options": ["A) input()", "B) print()", "C) scan()", "D) read()"], 
            "answer": "A"
        },
        
        {
            "question": "What will be the output of len('Python')?",
            "options": ["A) 5", "B) 6", "C) 7", "D) Error"], 
            "answer": "B"
        },

        {
            "question": "Which of the following operators has the highest precedence?",
            "options": ["A) % (Modulus)", "B) & (BitWise AND)", "C) ** (Exponent)", "D) > (Comparison)"],
            "answer": "C"
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
            "options": ["A) py", "B) yn", "C) pyn", "D) yna"],
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
            "question": "What is the output of the following code:\nfor i in range(10, 15, 1):\n\tprint( i, end=', ')",
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


def display_question(question_data, question_number):
    print("\n====================")
    print(f"Question {question_number}: {question_data['question']}\n")
    for option in question_data["options"]:
        print(option)


def get_user_answer():
    user_answer = input("Now enter your answer (A, B, C, D): ").strip().upper()
    if user_answer in ["A", "B", "C", "D"]:
        return user_answer
    else:
        return None


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Answer is correct!")
        return 1
    else:
        print(f"Your answer is wrong! The correct answer is {correct_answer}.")
        return 0


def update_score(score, result):
    if result:
        score += 1
    return score


def play_quiz():
    print("Welcome to Python Quiz!")
    # Get questions
    questions = get_questions()
    # Shuffle questions
    random.shuffle(questions)
    score = 0

    for i, question in enumerate(questions, start=1):
        display_question(question, i)
        countdown_timer()
        user_answer = get_user_answer()
        result = check_answer(user_answer, question["answer"])
        score = update_score(score, result)

    print(f"Your final score is: {score} / {len(questions)}")
    print("Thanks for playing!")

# --------------------------------------------------   

if __name__ == "__main__":
    play_quiz()
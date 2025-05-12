import random

def getRandomNumber():
    return random.randrange(1, 100)


def runGuess():
    secretNumber = getRandomNumber()
    print("The number is", secretNumber)


if __name__ == '__main__':
    runGuess()
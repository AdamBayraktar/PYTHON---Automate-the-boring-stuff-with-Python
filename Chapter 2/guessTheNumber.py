# It is program that ask you to guess the number that computer picked.

import random
# The range of number is constant and is between 1-20. It can be modified byt adding another random number to the end but not today:)
print("I am thinking number between 1 and 20")
# number that user have to guess
numberToGuess = random.randint(1,20)
# number of attemps made by user
userTries = 0
while True:
    userTries += 1
    print("Take a guess.")
    userGuess = int(input())
    if userGuess < numberToGuess:
        print("Your guess is too low.")
    elif userGuess > numberToGuess:
        print("Your guess is too high.")
    else:
        print(f"Good job! You guessed my number in {userTries} guesses!")
        break
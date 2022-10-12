# This program is answer to the 9th question of chapter 2.
# "Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam."

spam = [3]

# I decided to solve the question with creating function that checks if in variables is stored 1, 2, any data. If there is stored then program prints out appropiate sentences
def spam_checker(variableToCheck):
    if 1 in variableToCheck:
        print("Hello")
    if 2 in variableToCheck:
        print("Howdy")
    if variableToCheck:
        print("Greetings!")

spam_checker(spam)
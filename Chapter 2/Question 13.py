# "Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop."

# I have to write two loops that itterates the numbers from 1 to 10. One by using while loop the other by usign for loop

# let's start with for loop

for numberToPrint in range(1,11):
    print(numberToPrint)


# while loop. I created variable which initially is 0. Loop will increase variable by 1 and will print it out untill number 10 is achieved

whileLoopNumber = 0

while True:
    whileLoopNumber += 1
    print(whileLoopNumber)
    if whileLoopNumber == 10: break
    
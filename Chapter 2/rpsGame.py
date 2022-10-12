# It is simply rock, paper, scissors game

import random, sys

actionList = ['ROCK', 'PAPER', "SCISSORS"]

# hello to rock paper scissor game :)
print('ROCK, PAPER, SCISSORS')

# Variables that shows our score against computer 
numberOflosses = 0
numberOfWins = 0
numberOfDraws = 0


while True:
    
    #current game score
    print(f'{numberOfWins} Wins, {numberOflosses} Losses, {numberOfDraws} Ties')
    
    # program asks about to pick one of 4 possibilities 
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    listOfUserChoice = ['r','p','s','q']
    
    while True:
        userPick = input()
        
        # chceks whether user input correct value if not then asks again to enter
        if not (userPick in listOfUserChoice):
            print('Come on! Read again question and then submit your answer. (r, p, s or q to quit)')
            continue
        
        # change one letter input to rock, paper, scissors or if input is q then shut downs the program
        if userPick == 'r':
            print('ROCK versus...')
            userPick = 'ROCK'
        elif userPick == 'p':
            print('PAPER versus...')
            userPick = 'PAPER'
        elif userPick == 's':
            print('SCISSORS versus...')
            userPick = 'SCISSORS'
        elif userPick == 'q':
            print('Thank you for the game. Good bye Firend')
            sys.exit()

        # computer makes his choice and then compares it with user pick. The result is added to the score
        computerPick = actionList[random.randint(0,2)]
        print(computerPick)
        if userPick == computerPick:
            print('It is a tie!')
            numberOfDraws += 1
        elif (userPick == 'ROCK' and computerPick == 'PAPER') or (userPick == 'PAPER' and computerPick == 'SCISSORS') or (userPick == 'SCISSORS' and computerPick == 'ROCK'):
            print('You lose!')
            numberOflosses += 1
        else:
            print('You win!')
            numberOfWins += 1
        
        # if everythin went correct we will come to the break point in order to start another round
        break
        

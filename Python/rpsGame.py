import random, sys

print('ROCK, PAPER, SCISSORS')
#wins, losses, ties
wins = 0 
losses = 0 
ties = 0

while True: #main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # Player input loop
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #quit the game
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player loop
        print('Type one of r, p, s, or q')

    #display what the player chooses
    if playerMove == 'r':
        print('Rock vs...')
    elif playerMove == 'p':
        print('Paper vs...')
    elif playerMove == 's':
        print('Scissors vs...')

    #Display computer choice
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif randomNumber == 3:
        computerMove = 's'
        print('Scissors')

    #Display record
    if playerMove == computerMove:
        print('Tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose')
        losses = losses + 1
        
        

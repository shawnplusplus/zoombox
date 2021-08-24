#Random Number Guessing Game
import random
secretNumber = random.randint(1,20)
print('I\'m thinking of a number between 1 and 20')
#Ask for player input 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break #Correct guess condition

if guess == secretNumber:
    print('You guessed the right number in ' + str(guessesTaken) + ' guesses')
else: 
    print('Nope, the number I was thinking of was ' + str(secretNumber))     

import random
numberOfStreaks = 0
CoinFlip = []
streak = 0
# for ex in range(10000):
#   #print('Shawn')
#   #code that creates a list of 100 heads and tails values
#   flips = []
#   counter = 0
#   while len(flips) < 100:
#     f = random.randint(0, 1)
#     print(f)
#     print(len(flips))
#     if f == 1:
#       flips.append('H')
#     else:
#       flips.append('T')



#   #code that checks if there is a streak of 6 heads or tails in a row.


# print('Chance of streak: %s%%' % (numberOfStreaks / 100))


for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        CoinFlip.append(random.randint(0,1))
    #does not matter if it is 0 or 1, H or T, peas or lentils. I am going to check if there is multiple 0 or 1 in a row

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(CoinFlip)):
        if i==0:
            pass
        elif CoinFlip[i] == CoinFlip[i-1]:  #checks if current list item is the same as before
            streak += 1
        else:
            streak = 0

        if streak == 6:
            numberOfStreaks += 1
            print('Streak: ',  numberOfStreaks)

    # CoinFlip = []

print('Chance of streak: %s%%' % (numberOfStreaks / (100*10000)))
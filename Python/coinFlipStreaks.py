from pickle import APPEND
import random
numberOfStreaks = 0
for ex in range(10000):
  #print('Shawn')
  #code that creates a list of 100 heads and tails values
  flips = []
  counter = 0
  while len(flips) < 100:
    f = random.randint(0, 1)
    print(f)
    print(len(flips))
    if f == 1:
      flips.append('H')
    else:
      flips.append('T')



  #code that checks if there is a streak of 6 heads or tails in a row.


print('Chance of streak: %s%%' % (numberOfStreaks / 100))

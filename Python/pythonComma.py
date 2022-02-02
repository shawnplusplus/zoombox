spam = ['apples', 'bananas', 'tofu', 'cats']
emptyList = []

def printMyList(myList):
  concatList = ''
  if len(myList) > 0:
    for x in range(len(myList)):

      print(myList[x] + ', ', end='')
      # if x == len(myList):
      #   concatList += ', and ' + myList[x]
      #   print(concatList)
  else:
    print('There is nothing in the list.')
  return concatList




printMyList(spam)
# printMyList(emptyList)


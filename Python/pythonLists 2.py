import copy

spam = ['A', 'B', 'C', 'D']
print(spam)
print(id(spam))
cheese = copy.copy(spam)
print(cheese)
print(id(cheese))
cheese[1] = 42
print(spam)
print(cheese)



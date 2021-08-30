print ('Pick a number')
num = int(input())
print(num)
# print('Prime numbers between 0 and ',  objective)

# for x in range(0, objective + 1):
#     if x > 1:
#         for i in range(2, x):
#             if (x % 1) == 0:
#                 break
#         else:
#             print(x)


def isPrime(n):
    if (n <= 1):
        return False

    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

if isPrime(num):
    print('true')
else:
    print('False')    

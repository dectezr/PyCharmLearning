import math

n = int(input())
if n == 1:
    print('This number is not prime')
elif n == 2:
    print('This number is prime')
else:
    for k in range(2, math.floor(math.sqrt(n)) + 1):
        if n % k == 0:
            print('This number is not prime')
            break
    else:
        print('This number is prime')

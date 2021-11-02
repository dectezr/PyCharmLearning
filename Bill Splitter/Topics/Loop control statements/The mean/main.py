import numpy

numbers = []
while True:
    x = input()
    if x == '.':
        break
    else:
        numbers.append(int(x))
print(numpy.mean(numbers))

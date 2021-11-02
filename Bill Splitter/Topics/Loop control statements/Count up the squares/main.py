# put your python code here
number_sum = 0
square_sum = 0
while True:
    n = int(input())
    number_sum += n
    square_sum += pow(n, 2)
    if number_sum == 0:
        break
print(square_sum)

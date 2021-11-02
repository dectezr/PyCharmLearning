# put your code here
total = 0
count = 0
number = int(input())
while number != 55:
    total += number
    count += 1
    number = int(input())
print(count)
print(total)
print(round(total/count))

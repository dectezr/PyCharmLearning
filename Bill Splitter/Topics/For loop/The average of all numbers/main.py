# put your python code here
a = int(input())
b = int(input())
count = 0
sums = 0
for k in range(a, b + 1):
    if k % 3 == 0:
        count += 1
        sums += k
print(sums / count)

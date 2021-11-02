initial = int(input())
final = int(input())
period = 0
while final < initial:
    initial = initial/2
    period += 1
print(period * 12)
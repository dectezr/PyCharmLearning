initial = float(input())
deposit = 700000
years = 0
while initial <= deposit:
    initial *= 1+0.071
    years += 1
print(years)
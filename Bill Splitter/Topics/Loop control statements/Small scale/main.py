numbers = []
while True:
    x = input()
    if x == '.':
        break
    else:
        numbers.append(float(x))
print(min(numbers))

# Better Solution
# print(min(float(x) for x in iter(input, ".")))

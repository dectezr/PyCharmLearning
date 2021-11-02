# put your python code here
numbers = [int(number) for number in input().split()]
index = int(input())
positions = [i for i in range(len(numbers)) if numbers[i] == index]
if not positions:
    print('not found')
else:
    print(*positions)

# print(" ".join(idx) if idx else "not found") # Better ones

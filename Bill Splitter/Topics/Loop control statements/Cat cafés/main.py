max_number = 0
while True:
    pair = input().split()
    if pair[0] == 'MEOW':
        break
    elif int(pair[1]) > max_number:
        cafe = pair[0]
        max_number = int(pair[1])
print(cafe)

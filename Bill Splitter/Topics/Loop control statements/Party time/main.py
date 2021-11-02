friends = []
while True:
    name = input()
    if name != '.':
        friends.append(name)
    else:
        break
print(friends)
print(len(friends))

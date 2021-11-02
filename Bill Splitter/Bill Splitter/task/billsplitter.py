# write your code here
import random

print('Enter the number of friends joining (including you):')
numbers = int(input())
if numbers > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    friends_name = []
    for _ in range(numbers):
        friends_name.append(input())
    print('Enter the total bill value:')
    total = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer == "Yes":
        name = random.choice(friends_name)
        print(name, 'is the lucky one!')
        share = round(total / (numbers - 1), 2)
        friends = dict.fromkeys(friends_name, share)
        friends[name] = 0
    else:
        print('No one is going to be lucky')
        share = round(total / numbers, 2)
        friends = dict.fromkeys(friends_name, share)
    print(friends)
else:
    print('No one is joining for the party')

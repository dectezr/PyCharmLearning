chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769
money = int(input())
if money < chicken:
    print('None')
elif money < goat:
    print(str(money // chicken) + ' chickens' if money // chicken != 1 else '1 chicken')
elif money < pig:
    print(str(money // goat) + ' goats' if money // goat != 1 else '1 goat')
elif money < cow:
    print(str(money // pig) + ' pigs' if money // pig != 1 else '1 pig')
elif money < sheep:
    print(str(money // cow) + ' cows' if money // cow != 1 else '1 cow')
else:
    print(str(money // sheep) + ' sheep')

# Better Solution
# money = int(input())
# price = {"sheep": 6769, "cow": 3848, "pig": 1296, "goat": 678, "chicken": 23}
#
# if money < price['chicken']:
#     print('None')
# else:
#     for animal, cost in price.items():
#         if money >= cost:
#             n = money // cost
#             output = animal + 's' if n > 1 and animal != 'sheep' else animal
#             print(n, output)
#             break

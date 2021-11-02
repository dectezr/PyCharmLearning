cards = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
for i in range(2, 11):
    cards.update({str(i): i})
count = 0
for _ in range(6):
    count += cards[input()]
print(count / 6)

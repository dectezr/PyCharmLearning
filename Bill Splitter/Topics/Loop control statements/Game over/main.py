scores = input().split()
# put your python code here
count = 0
loss = 0
for char in scores:
    if char == 'C':
        count += 1
    else:
        loss += 1
        if loss == 3:
            print('Game over')
            break
else:
    print('You won')
print(count)

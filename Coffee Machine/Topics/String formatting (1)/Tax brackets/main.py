income = int(input())
if income <= 15527:
    rate = 0
elif income <= 42707:
    rate = 15
elif income <= 132406:
    rate = 25
else:
    rate = 28
print(
    'The tax for {0} is {1}%. That is {2} dollars!'.format(income, rate, round(income * rate / 100)))

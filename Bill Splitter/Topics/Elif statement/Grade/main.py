score = int(input())
maximum = int(input())
rate = score / maximum
if rate < 0.6:
    print('F')
elif rate < 0.7:
    print('D')
elif rate < 0.8:
    print('C')
elif rate < 0.9:
    print('B')
else:
    print('A')
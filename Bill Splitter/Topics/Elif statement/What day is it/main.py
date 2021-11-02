reference_time = 10.5
zone = int(input())
if reference_time + zone < 0:
    print('Monday')
elif reference_time + zone > 24:
    print('Wednesday')
else:
    print('Tuesday')
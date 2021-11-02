cum_sum = [int(number) for number in input()]
cum_sum = [sum(cum_sum[:i + 1]) for i in range(len(cum_sum))]
print(cum_sum)

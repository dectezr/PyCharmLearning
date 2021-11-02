number_string = input()
numbers = [int(number) for number in number_string]
running_average = []
for i in range(len(numbers) - 1):
    running_average.append((numbers[i] + numbers[i + 1]) / 2.0)
print(running_average)

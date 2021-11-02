import random
MAX_LENGTH = 100

print('Please give AI some data to learn...')
number_list = []
while len(number_list) < MAX_LENGTH:
    print(f'The current data length is {len(number_list)}, {MAX_LENGTH - len(number_list)} symbols left')
    number_list.extend([n for n in input('Print a random string containing 0 or 1:') if n in ['0', '1']])
print('Final data string:')
print(''.join(number_list))

slice_list = [''.join(number_list[i:i+4]) for i in range(len(number_list) - 3)]
compare_list = [str(bin(n)[2:]).rjust(3, '0') for n in range(0, 8)]
# dictionary = {char: f'{slice_list.count(char + "0")},{slice_list.count(char + "1")}' for char in compare_list}
dictionary = {char: [slice_list.count(char + "0"), slice_list.count(char + "1")] for char in compare_list}
# for (key, value) in dictionary.items():
#     print(key + ':', value)

print('You have $1000. Every time the system successfully predicts your next press, you lose $1.')
print('Otherwise, you earn $1. Print "enough" to leave the game.', "Let's go!")
capital = 1000

while True:
    command = input('Print a random string containing 0 or 1:\n')
    if command == 'enough':
        print('Game over!')
        break
    new_list = [n if n in ['0', '1'] else False for n in command]
    if False in new_list:
        continue
    total_counts = len(new_list) - 3
    prediction_list = [random.choice(number_list) for _ in range(3)]
    right_counts = 0
    for i in range(3, len(new_list)):
        chars = dictionary[''.join(new_list[i - 3:i])]
        prediction_list.append(f'{chars.index(max(chars))}' if chars[0] != chars[1] else random.choice(['0', '1']))
        if prediction_list[i] == new_list[i]:
            right_counts += 1
    capital += total_counts - 2 * right_counts
    rate = round(right_counts * 100 / total_counts, 2)
    print('prediction:')
    print(''.join(prediction_list))
    print()
    print(f'Computer guessed right {right_counts} out of {total_counts} symbols ({rate} %)')
    print(f'Your capital is now ${capital}')
    print()
    # dictionary update. Same codes as before loop
    number_list.extend(new_list)
    slice_list = [''.join(number_list[i:i + 4]) for i in range(len(number_list) - 3)]
    dictionary = {char: [slice_list.count(char + "0"), slice_list.count(char + "1")] for char in compare_list}

word = input()
for char in ',.!?':
    word = word.replace(char, '')
word = word.lower()
print(word)
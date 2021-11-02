string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
numbers = 0
for vowel in string:
    if vowel in vowels:
        numbers += 1
print(numbers)
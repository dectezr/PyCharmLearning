vowel = 'aeiou'
sequence = input()
for char in sequence:
    if ord(char) < ord('a') or ord(char) > ord('z'):
        break
    elif char in vowel:
        print('vowel')
    else:
        print('consonant')

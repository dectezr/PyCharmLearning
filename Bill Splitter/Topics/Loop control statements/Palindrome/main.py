word = list(input())
for i in range(len(word)):
    if word[i] != word[len(word)-i-1]:
        print('Not palindrome')
        break
else:
    print('Palindrome')
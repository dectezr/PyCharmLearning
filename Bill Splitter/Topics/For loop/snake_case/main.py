phrase = input()
if ~phrase.islower():
    phrase = list(phrase)
    n = len(phrase)
    for i in range(n):
        if phrase[n - i - 1].isupper():
            phrase[n - i - 1] = phrase[n - i - 1].lower()
            if n - i - 1 != 0:
                phrase.insert(n - i - 1, '_')
        # 　print(i,phrase)
    phrase = ''.join(phrase)
print(phrase)

# Better solution as below
# word = input()
# print(word[0].lower() + ''.join("_" + c.lower() if c.upper() == c else c for c in word[1::]))

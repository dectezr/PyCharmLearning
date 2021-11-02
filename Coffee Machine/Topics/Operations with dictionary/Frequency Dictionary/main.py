# put your python code here
words = list((input().lower()).split())
line = {}
for word in words:
    if word in line:
        line[word] += 1
    else:
        line[word] = 1
for (key, value) in line.items():
    print(key, value)

# Better Solution
# def words(line):
#     line_dict = {x: line.count(x) for x in line}
#     for k, v in line_dict.items():
#         print(k, v)
#
# words(input().lower().split())

# Another Solution
# words = input().lower().split()
# for word in set(words):
#     print(word, words.count(word))

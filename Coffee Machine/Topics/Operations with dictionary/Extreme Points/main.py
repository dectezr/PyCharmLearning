# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
key = list(test_dict.keys())
value = list(test_dict.values())
print('min:', key[value.index(min(value))])
print('max:', key[value.index(max(value))])

# Better Solution
# print("min:", min(test_dict, key=test_dict.get))
# print("max:", max(test_dict, key=test_dict.get))

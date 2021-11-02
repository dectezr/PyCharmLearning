name = input()


def normalize(name):
    # put your code here
    replace_dict = {'é': 'e', 'ë': 'e', 'á': 'a', 'å': 'a', 'œ': 'oe', 'æ': 'ae'}
    for key, value in replace_dict.items():
        name = name.replace(key, value)
    return name


print(normalize(name))

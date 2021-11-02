# read sums.txt
filename = 'hyperskill-dataset-42615895.txt'
file = open(filename, 'r')
summer_dict = dict()
for line in file:
    words = line.split()
    for word in words:
        if word in summer_dict:
            summer_dict[word] += 1
        else:
            summer_dict[word] = 1
print(f'Word "summer" times: {summer_dict["summer"]}')
file.close()

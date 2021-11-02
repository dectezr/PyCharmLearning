n = int(input())
name_list = []
for _ in range(n):
    result = input()
    result = result.split()
    if result[1] == 'win':
        name_list.append(result[0])
print(name_list)
print(len(name_list))

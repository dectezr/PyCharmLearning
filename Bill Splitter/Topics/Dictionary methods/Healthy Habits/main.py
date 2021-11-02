# the list "walks" is already defined
# your code here
count = 0
for days in walks:
    count += days['distance']
print(count // len(walks))

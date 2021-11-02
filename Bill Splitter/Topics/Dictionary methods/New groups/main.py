# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
classes = {}
numbers = int(input())
for i in range(len(groups)):
    if i < numbers:
        classes.update({groups[i]: int(input())})
    else:
        classes.update({groups[i]: None})
print(classes)

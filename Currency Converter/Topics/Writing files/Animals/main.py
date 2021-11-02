# read animals.txt
# and write animals_new.txt
old_file = open('animals.txt')
new_file = open('animals_new.txt', 'w')
for line in old_file:
    new_file.write(line.rstrip('\n') + ' ')
old_file.close()
new_file.close()

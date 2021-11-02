# read sums.txt
file = open("sums.txt")
for line in file:
    print(sum(int(n) for n in line.split()))
file.close()

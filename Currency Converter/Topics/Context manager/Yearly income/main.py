# write your code here
with open('salary.txt') as f1, \
     open('salary_year.txt', 'w') as f2:
    f2.writelines([str(int(x.strip('\n')) * 12) + '\n' for x in f1.readlines()])

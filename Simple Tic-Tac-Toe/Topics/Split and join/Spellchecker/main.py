dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
correct = True
for word in input().split():
    if word not in dictionary:
        print(word)
        correct = False
if correct:
    print('OK')

# Write your code here
import random

print('H A N G M A N')
while input('Type "play" to play the game, "exit" to quit: ') == 'play':
    answer = random.choice(['python', 'java', 'kotlin', 'javascript'])
    reveal = list('-' * len(answer))
    lifecounts = 8
    guessed = []
    while lifecounts > 0 and ''.join(reveal) != answer:
        print()
        print(''.join(reveal))
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print('You should input a single letter')
        elif not letter.islower():
            print('Please enter a lowercase English letter')
        elif letter in reveal or letter in guessed:
            print("You've already guessed this letter")
        elif letter in answer:
            for j in range(len(answer)):
                if answer[j] == letter:
                    reveal[j] = letter
        else:
            print("That letter doesn't appear in the word")
            lifecounts -= 1
            guessed.append(letter)
    if lifecounts == 0:
        print('You lost!')
    else:
        print('You guessed the word!')
        print('You survived!')
    print()












# word = input(f'Guess the word {answer[0:3] + (len(answer) - 3) * "-"}:')
# if word == answer:
#     print('You survived!')
# else:
#     print('You lost!')

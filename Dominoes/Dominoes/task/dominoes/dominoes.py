# Notice that this code is not functionalized into parts and has no notes, so it may be hard to read anyway.
import random

full_cards = []
for i in range(7):
    full_cards.extend([[j, i] for j in range(i + 1)])
status = None
computer_pieces, left, player_pieces, stock_pieces, domino_snake = [], [], [], [], []
while status is None:
    computer_pieces = random.sample(full_cards, k=7)  # or random.shuffle
    left = [x for x in full_cards if x not in computer_pieces]
    player_pieces = random.sample(left, k=7)
    stock_pieces = [x for x in left if x not in player_pieces]
    for i in range(6, -1, -1):
        domino_snake = [i, i]
        if domino_snake in player_pieces:
            player_pieces.remove(domino_snake)
            status = 'computer'
            break
        elif domino_snake in computer_pieces:
            computer_pieces.remove(domino_snake)
            status = 'player'
            break
    domino_snake = [domino_snake]
# print('Stock pieces:', stock_pieces)
# print('Computer pieces:', computer_pieces)
# print('Player pieces:', player_pieces)
# print('Domino snake:', domino_snake)
# print('status: ' + status)

while True:
    print('=' * 70)
    print('Stock size:', len(stock_pieces))
    print('Computer pieces:', len(computer_pieces))
    print()
    snake = ''
    if len(domino_snake) <= 6:  # print(self.domino_snake[i], end='')
        for x in domino_snake:
            snake += str(x)
    else:  # print(" ".join(map(str, self.domino_snake[0:3])), '...', " ".join(map(str, self.domino_snake[-4:-1])))
        for i in range(3):
            snake += str(domino_snake[i])
        snake += '...'
        for i in range(len(domino_snake) - 3, len(domino_snake)):
            snake += str(domino_snake[i])
    print(snake)
    print()
    print('Your pieces:')
    for i in range(len(player_pieces)):
        print(f'{i + 1}:{player_pieces[i]}')
    print()
    if status == 'player':
        print("Status: It's your turn to make a move. Enter your command.")
        right_command = False
        command = None
        while right_command is False:
            try:
                command = int(input())
                if abs(command) > len(player_pieces):
                    print('Invalid input. Please try again.')
                elif command == 0 and len(stock_pieces) == 0:
                    status = 'draw'
                    right_command = True
                elif command < 0 and domino_snake[0][0] not in player_pieces[abs(command) - 1]:
                    print('Illegal move. Please try again.')
                elif command > 0 and domino_snake[len(domino_snake) - 1][1] not in player_pieces[abs(command) - 1]:
                    print('Illegal move. Please try again.')
                else:
                    right_command = True
            except ValueError:
                print('Invalid input. Please try again.')
        if status != 'draw':
            if command == 0:
                new = random.choice(stock_pieces)
                stock_pieces.remove(new)
                player_pieces.append(new)
            elif command < 0:
                command = -command
                if domino_snake[0][0] == player_pieces[command - 1][0]:
                    player_pieces[command - 1] = player_pieces[command - 1][::-1]
                domino_snake.insert(0, player_pieces.pop(command - 1))
            else:
                if domino_snake[len(domino_snake) - 1][1] == player_pieces[command - 1][1]:
                    player_pieces[command - 1] = player_pieces[command - 1][::-1]
                domino_snake.insert(len(domino_snake), player_pieces.pop(command - 1))
            if not player_pieces:
                status = 'win'
            else:
                status = 'computer'
    elif status == 'computer':
        print("Status: Computer is about to make a move. Press Enter to continue...")
        input()
        # # TODO
        number_points = {str(i): 0 for i in range(7)}
        for i in range(7):
            for x in computer_pieces + domino_snake:
                number_points[str(i)] += x.count(i)
        card_points = []
        for i in range(len(computer_pieces)):
            card_points.append([number_points[str(computer_pieces[i][0])] + number_points[str(computer_pieces[i][1])], i])
        card_points = sorted(card_points, key=lambda cards: cards[0])
        flag_found = None
        for x in card_points:
            card = computer_pieces[x[1]]
            if domino_snake[0][0] in card:
                if domino_snake[0][0] == card[0]:
                    card_rev = card[::-1]
                    domino_snake.insert(0, card_rev)
                else:
                    domino_snake.insert(0, card)
                computer_pieces.remove(card)
                flag_found = True
                break
            elif domino_snake[len(domino_snake) - 1][1] in card:
                if domino_snake[len(domino_snake) - 1][1] == card[1]:
                    card_rev = card[::-1]
                    domino_snake.append(card_rev)
                else:
                    domino_snake.append(card)
                computer_pieces.remove(card)
                flag_found = True
                break
        if flag_found is None:
            if not stock_pieces:
                status = 'draw'
            else:
                new = random.choice(stock_pieces)
                stock_pieces.remove(new)
                computer_pieces.append(new)
        if not computer_pieces:
            status = 'lose'
        else:
            status = 'player'
    elif status == 'win':
        print('Status: The game is over. You won!')
        break
    elif status == 'lose':
        print('Status: The game is over. The computer won!')
        break
    elif status == 'draw':
        print("Status: The game is over. It's a draw!")
        break
    if domino_snake[0][0] == domino_snake[len(domino_snake) - 1][1]:
        n = domino_snake[0][0]
        count = 0
        for x in domino_snake:
            count += x.count(n)
        if count == 10:
            status = 'draw'


#       while True:
#             index = random.randint(-len(computer_pieces), len(computer_pieces))
#             if index == 0:
#                 if not stock_pieces:
#                     status = 'draw'
#                     break
#                 computer_pieces.append(stock_pieces.pop(random.randint(0, len(stock_pieces) - 1)))
#                 break
#             elif index < 0 and domino_snake[0][0] in computer_pieces[abs(index) - 1]:
#                 if domino_snake[0][0] == computer_pieces[abs(index) - 1][0]:
#                     computer_pieces[abs(index) - 1] = computer_pieces[abs(index) - 1][::-1]
#                 domino_snake.insert(0, computer_pieces[abs(index) - 1])
#                 computer_pieces.pop(abs(index) - 1)
#                 break
#             elif index > 0 and domino_snake[len(domino_snake) - 1][1] in computer_pieces[index - 1]:
#                 if domino_snake[len(domino_snake) - 1][1] == computer_pieces[index - 1][1]:
#                     computer_pieces[index - 1] = computer_pieces[index - 1][::-1]
#                 domino_snake.append(computer_pieces[index - 1])
#                 computer_pieces.pop(index - 1)
#                 break
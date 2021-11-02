def print_positions(string):
    print(f"""---------
    | {string[0]} {string[1]} {string[2]} |
    | {string[3]} {string[4]} {string[5]} |
    | {string[6]} {string[7]} {string[8]} |
    ---------""")


def position_check(string, position):
    try:
        x_coor, y_coor = position.split()
        x_coor = int(x_coor)
        y_coor = int(y_coor)
    except (TypeError, ValueError):
        print('You should enter numbers!')
        return False
    if x_coor not in [1, 2, 3] or y_coor not in [1, 2, 3]:
        print('Coordinates should be from 1 to 3!')
        return False
    if string[(x_coor - 1) * 3 + (y_coor - 1)] != '_':
        print('This cell is occupied! Choose another one!')
        return False
    return True


def status_check(string):
    X_count = O_count = 0
    for step in range(0, 9, 3):  # 横向
        if string[step] == string[step + 1] and string[step] == string[step + 2]:
            if string[step] == 'X':
                X_count += 1
            elif string[step] == 'O':
                O_count += 1
    for step in range(3):  # 纵向
        if string[step] == string[step + 3] and string[step] == string[step + 6]:
            if string[step] == 'X':
                X_count += 1
            elif string[step] == 'O':
                O_count += 1
    if string[4] == string[0] and string[4] == string[8]:  # 左斜对角
        if string[4] == 'X':
            X_count += 1
        elif string[4] == 'O':
            O_count += 1
    if string[4] == string[2] and string[4] == string[6]:  # 右斜对角
        if string[4] == 'X':
            X_count += 1
        elif string[4] == 'O':
            O_count += 1
    if X_count > 0:
        print('X wins')
        return True
    elif O_count > 0:
        print('O wins')
        return True
    elif '_' not in string:
        print('Draw')
        return True
    else:
        # print('Game not finished')
        return False


def making_move(string):
    position = input('Enter the coordinates:')
    while not position_check(string, position):
        position = input('Enter the coordinates:')
    x_coor, y_coor = position.split()
    index = (int(x_coor) - 1) * 3 + (int(y_coor) - 1)
    if string.count('_') % 2 == 1:
        return string[0:index] + 'X' + string[index + 1:]
    else:
        return string[0:index] + 'O' + string[index + 1:]


string = '_' * 9
print_positions(string)
while not status_check(string):
    string = making_move(string)
    print_positions(string)


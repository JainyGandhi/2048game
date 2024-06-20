import random

def start_game():
    mat = []
    print("A to move left, D to move right, W to move up and S to move down")
    for i in range(0, 4):
        mat.append([0] * 4)
    add_two_random_start(mat)
    return mat

def random_one_addition(mat):
    zero_positions = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if zero_positions:
        i, j = random.choice(zero_positions)
        mat[i][j] = random.choice([2, 4])
    return mat

def add_two_random_start(mat):
    zero_positions = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if zero_positions:
        r1, c1 = random.choice(zero_positions)
        zero_positions.remove((r1, c1))  # Remove the first chosen position
        if zero_positions:  # If there are more zero positions available
            r2, c2 = random.choice(zero_positions)
            mat[r1][c1] = random.choice([2, 4])
            mat[r2][c2] = random.choice([2, 4])
    return mat

def check_game(mat):
    for i in range(0, 4):
        for j in range(0, 4):
            if mat[i][j] == 2048:
                print('Congratulations, you reached 2048!')
                return True
    return False

def merge_tiles_move_left(mat):
    # Shifting tiles to the left
    for i in range(4):
        filtered = [num for num in mat[i] if num != 0]
        filtered += [0] * (4 - len(filtered))
        mat[i] = filtered

    # Merging tiles
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0

    # Shifting tiles to the left again
    for i in range(4):
        filtered = [num for num in mat[i] if num != 0]
        filtered += [0] * (4 - len(filtered))
        mat[i] = filtered

    return mat

def merge_tiles_move_right(mat):
    # Shifting tiles to the right
    for i in range(4):
        filtered = [num for num in mat[i] if num != 0]
        filtered = [0] * (4 - len(filtered)) + filtered
        mat[i] = filtered

    # Merging tiles
    for i in range(4):
        for j in range(3, 0, -1):
            if mat[i][j] == mat[i][j - 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j - 1] = 0

    # Shifting tiles to the right again
    for i in range(4):
        filtered = [num for num in mat[i] if num != 0]
        filtered = [0] * (4 - len(filtered)) + filtered
        mat[i] = filtered

    return mat

def merge_tiles_move_up(mat):
    for j in range(4):
        filtered = [mat[i][j] for i in range(4) if mat[i][j] != 0]
        filtered += [0] * (4 - len(filtered))
        for i in range(4):
            mat[i][j] = filtered[i]

    for j in range(4):
        for i in range(3):
            if mat[i][j] == mat[i + 1][j] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i + 1][j] = 0

    for j in range(4):
        filtered = [mat[i][j] for i in range(4) if mat[i][j] != 0]
        filtered += [0] * (4 - len(filtered))
        for i in range(4):
            mat[i][j] = filtered[i]

    return mat

def merge_tiles_move_down(mat):
    for j in range(4):
        filtered = [mat[i][j] for i in range(4) if mat[i][j] != 0]
        filtered = [0] * (4 - len(filtered)) + filtered
        for i in range(4):
            mat[i][j] = filtered[i]

    for j in range(4):
        for i in range(3, 0, -1):
            if mat[i][j] == mat[i - 1][j] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i - 1][j] = 0

    for j in range(4):
        filtered = [mat[i][j] for i in range(4) if mat[i][j] != 0]
        filtered = [0] * (4 - len(filtered)) + filtered
        for i in range(4):
            mat[i][j] = filtered[i]

    return mat

def move_tiles(move, mat):
    if move == 'A':
        merge_tiles_move_left(mat)
    elif move == 'D':
        merge_tiles_move_right(mat)
    elif move == 'W':
        merge_tiles_move_up(mat)
    elif move == 'S':
        merge_tiles_move_down(mat)
    else:
        print("Invalid move")
    return mat

def is_game_over(mat):
    if any(0 in row for row in mat):
        return False
    for i in range(4):
        for j in range(4):
            if (i < 3 and mat[i][j] == mat[i + 1][j]) or (j < 3 and mat[i][j] == mat[i][j + 1]):
                return False
    return True

def operation(mat):
    while not check_game(mat):
        if is_game_over(mat):
            print("Game Over!")
            break
        move = input("Enter the command: ")
        if move in ['A', 'D', 'W', 'S']:
            mat = move_tiles(move, mat)
            random_one_addition(mat)
            print_board(mat)
        else:
            print("Invalid command, please try again.")

def print_board(mat):
    for row in mat:
        print(row)

game_matrix = start_game()
print_board(game_matrix)
operation(game_matrix)

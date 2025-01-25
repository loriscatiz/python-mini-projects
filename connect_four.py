import sys
sys.path.append('../modules')
from modules import utils

numbers = ["1️⃣", "2️⃣","3️⃣","4️⃣", "5️⃣", "6️⃣", "7️⃣",]

board: list[list[str]] = [
    [ '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵'],
    [ '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵'],
    [ '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵'],
    [ '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵'],
    [ '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵'],
    [ '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵'],
    ]

height = len(board)
width = len(board[0])

max_turns = height * width

def print_board():
    for num in numbers:
        print(num, end= "  ")
    print()
    for row in board:
        for e in row:
            print(e, end=' ')
        print()

def switch_player(player: str) -> str:
    player = '🔴' if player == '🟡' else '🟡'
    return player

def insert_into(col_index: int, player: str) -> list[int] | bool:
    for i in range(height):
        if board[0][col_index] != '🔵':
            print(f"The column {col_index + 1} is already full")
            print_board()
            return False 
        if board[height-1 - i][col_index] == '🔵': 
            board[height-1 - i][col_index] = player 
            return [height-1 - i, col_index]
    return False

def check_horizontal(coordinates: list[int], player: str):
    y = coordinates[0]
    x = coordinates[1]
    checker:str = ''
    for i in range(4):
        try:
            if board[y][x+i] == player:
                checker += player
            else:
                break
        except IndexError:
            break
    for i in range(1, 4):
        try:
            if x-i < 0:
                raise IndexError
            if board[y][x-i] == player:
                checker += player
            else:
                break
        except IndexError:
            break
    if player * 4 in checker:
        return True
    return False

def check_vertical(coordinates: list[int], player: str):
    y = coordinates[0]
    x = coordinates[1]
    checker:str = ''
    for i in range(4):
        try:
            if board[y+i][x] == player:
                checker += player
            else:
                break
        except IndexError:
            break
    if player * 4 in checker:
        return True
    return False

def check_diagonal_to_top_left(coordinates: list[int], player: str):
    y = coordinates[0]
    x = coordinates[1]
    checker:str = ''
    for i in range(4):
        try:
            if board[y+i][x+i] == player:
                checker += player
            else:
                break
        except IndexError:
            break
    for i in range(1, 4):
        try:
            if y-i < 0 or x-i < 0:
                raise IndexError
            if board[y-i][x-i] == player:
                checker += player
            else:
                break
        except IndexError:
            break
    if player * 4 in checker:
        return True
    return False

def check_diagonal_to_top_right(coordinates: list[int], player: str):
    y = coordinates[0]
    x = coordinates[1]
    checker:str = ''
    for i in range(4):
        try:
            if  x-i < 0:
                raise IndexError
            if board[y+i][x-i] == player:
                checker += player
            else:
                break
        except IndexError:
            break
    for i in range(1, 4):
        try:
            if  y-i < 0:
                raise IndexError
            if board[y-i][x+i] == player:
                checker += player
            else:
                break
        except IndexError:
            break
    if player * 4 in checker:
        return True
    return False

def check_win(coordinates: list[int], player: str) -> bool:
    conditions: list[bool] = [
        check_horizontal(coordinates, player),
        check_vertical(coordinates, player),
        check_diagonal_to_top_left(coordinates, player),
        check_diagonal_to_top_right(coordinates, player),]
    if True in conditions:
        return True
    return False

def engine(usernames: tuple[str, str], win_count :list[int]):
    print_board()
    player = "🔴"
    turn = 1
    running = True
    while running == True:
        print(f"turn #{turn}")
        player_username = usernames[0] if turn % 2 else usernames[1]
        print(f"{player} {player_username}'s turn")
        print("Select the column you want to insert your token")
        col_index = utils.get_int_in_range(1, 7) - 1
        coordinates = insert_into(col_index, player)
        if not coordinates is False: 
            win = check_win(coordinates, player) #type: ignore
            print_board()
            if win:
                print(f"{player} {player_username} wins the game")
                running = False
            else:
                player = switch_player(player)
                turn +=1
            if turn > max_turns:
                print(f"The game is a draw")
                running = False

def main():
    print(f"Player 1 🔴 insert your username:")
    player_1 = utils.get_string_in_range(3, 12)
    print(f"Player 2 🟡 insert your username:")
    player_2 = utils.get_string_in_range(3, 12)
    usernames = (player_1, player_2)
    win_count: list[int] = [0, 0]
    engine(usernames, win_count)

if __name__ == '__main__':
    main()
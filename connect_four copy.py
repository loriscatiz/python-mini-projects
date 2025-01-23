import sys
sys.path.append('../modules')
from modules import utils

class ColumnFull(IndexError):
    pass
class OutOfBoard(IndexError):
    pass
class DeadEnd(IndexError):
    pass

board: list[list[str]] = [
    [ '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵'],
    [ '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵'],
    [ '🔵',  '🔴',  '🔵',  '🔵',  '🔵',  '🔵',  '🔴'],
    [ '🔵',  '🟡',  '🔵',  '🔵',  '🔵',  '🔴',  '🔴'],
    [ '🔵',  '🟡',  '🟡',  '🔴',  '🔵',  '🔴',  '🔴'],
    [ '🔵',  '🟡',  '🟡',  '🔴',  '🔴',  '🔴',  '🔴'],
    ]


numbers = [
        "1️⃣",
        "2️⃣",
        "3️⃣",
        "4️⃣",
        "5️⃣",
        "6️⃣",
        "7️⃣",

     ]

height = len(board)
width = len(board[0])

def print_board():
    for num in numbers:
        print(num, end= "  ")
    print()
    for row in board:
        for e in row:
            print(e, end=' ')
        print()

print(f"height: {height}")
print(f"width: {width}")

def insert_into(col_index: int, player: str) -> list[int]: # type: ignore
    for i in range(height):
        if board[0][col_index] != '🔵':
            return False # type: ignore
        if board[height-1 - i][col_index] == '🔵': 
            board[height-1 - i][col_index] = player 
            return [height-1 - i, col_index]

def check_horizontal(coordinates: list[int], player: str):
    y = coordinates[0]
    x = coordinates[1]
    checker:str = ''
    for i in range(4):
        try:
            if board[y][x+i] == player:
                checker += player
                print(checker)
            else:
                break
        except IndexError:
            break
    for i in range(3):
        try:
            if board[y][x-i-1] == player:
                checker += player
                print(checker)
            else:
                break
        except IndexError:
            break
    if player * 4 in checker:
        print('Win')
        return True

def check_vertical(coordinates: list[int], player: str):
    y = coordinates[0]
    x = coordinates[1]
    checker:str = ''
    for i in range(4):
        try:
            if board[y+i][x] == player:
                checker += player
                print(checker)
            else:
                break
        except IndexError:
            break
    if player * 4 in checker:
        print('Win')
        return True


def check_diagonal_one(coordinates: list[int], player: str):
    y = coordinates[0]
    x = coordinates[1]
    checker:str = ''
    for i in range(4):
        try:
            if board[y+i][x+i] == player:
                checker += player
                print(checker)
            else:
                break
        except IndexError:
            break
    for i in range(3):
        try:
            if board[y-i-1][x-i-1] == player:
                checker += player
                print(checker)
            else:
                break
        except IndexError:
            break
    if player * 4 in checker:
        print('Win')
        return True




def check_diagonal_two(coordinates: list[int], player: str):
    y = coordinates[0]
    x = coordinates[1]
    checker:str = ''
    for i in range(4):
        try:
            if board[y-i][x+i] == player:
                checker += player
                print(checker)
            else:
                break
        except IndexError:
            break
    for i in range(3):
        try:
            if board[y+i-1][x-i-1] == player:
                checker += player
                print(checker)
            else:
                break
        except IndexError:
            break
    if player * 4 in checker:
        print('Win')
        return True





def main():
    print("Horizontal test")
    print_board()
    insert_into(3, "🔴")
    print_board()
    check_horizontal([height-1, 3], "🔴")

    print()
    print()
    print("Vertical test")
    print_board()
    insert_into(6, "🔴")
    print_board()
    check_vertical([2, 6], "🔴")

    print()
    print()
    print("Diagonal test 1")
    print_board()
    insert_into(2, "🔴")
    print_board()
    check_diagonal_one([3, 2], "🔴")


    print()
    print()
    print("Diagonal test 2")
    print_board()
    insert_into(4, "🔴")
    print_board()
    check_diagonal_two([4, 4], "🔴")




if __name__ == '__main__':
    main()

"""
def switch_player(player: str) -> str:
    player = '🔴' if player == '🟡' else '🟡'
    return player
"""
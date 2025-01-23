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
    [ '🔵',  '🔵',  '🔵',  '🔴',  '🔵',  '🔵',  '🔵'],
    [ '🔵',  '🔵',  '🟡',  '🟡',  '🔵',  '🔵',  '🔵'],
    [ '🔵',  '🔴',  '🟡',  '🟡',  '🔴',  '🔴',  '🔵'],
    [ '🔴',  '🟡',  '🟡',  '🟡',  '🔵',  '🔴',  '🔴'],
    ]


def switch_player(player: str) -> str:
    player = '🔴' if player == '🟡' else '🟡'
    return player

def is_valid_column(column: int) -> None:
    if column > len(board) + 1:
        raise OutOfBoard
    if board[0][column - 1] != ' ':
        raise ColumnFull
    
def update_column(player: str, column: int):
    for i in range(len(board)):
        i = -i - 1
        if board[i][column-1] == '🔵':
            board[i][column - 1] = player
            return [abs(i), column] # coordinates of the thing 

def insert_into_col(column: int, player: str) -> list[int]:
            if column > len(board) + 1:
                raise OutOfBoard
            if board[0][column - 1] != '🔵':
                raise ColumnFull
            coordinates = update_column(player , column)
            coordinates[0] = - coordinates[0] #type: ignore
            coordinates[1] = coordinates [1] - 1 #type: ignore
            return coordinates # type: ignore
        
"""        
def check_win_vert(coordinates: list[int], player: str):    
    retvalue = True
    try:
        for i in range(4):
            if board[coordinates[0]+i][coordinates[1]] == player:
                continue
            else:
                retvalue = False
                return retvalue
    except IndexError:
        retvalue = False
    finally:
        return retvalue

def check_win_horiz(coordinates: list[int], player: str):
    color_count = -1

    for i in range(4):
        try:
            if board[coordinates[0]][coordinates[1] + i] == player:
                color_count += 1
                print(color_count)
                continue
            else:
                break
        except IndexError:
            break
    
    for j in range(4-color_count):
        try:
            if board[coordinates[0]][coordinates[1] - j] == player:
                color_count += 1
                print(color_count)
                continue
            else:
                break
        except IndexError:
            break
    if color_count == 4:
        return True
    else:
        return False """

""" def check_win_diag_up(coordinates: list[int], player: str):   
    diag_list = [board[coordinates[0]][coordinates[1]]]
    coordinates = list(map(abs, coordinates))
    i = 1
    while i < 4:
        try:
            diag_list.append(board[-len(board) + coordinates[0] + i][ - len(board[0]) + coordinates[1] + i])
            print([coordinates[0] + i], [coordinates[1] + i])
            print(diag_list)
            i+=1
        except IndexError:
            break
    
    j = 1
    while j < 4:
        try:
            diag_list.insert(0, board[-len(board) + coordinates[0] + j][ - len(board[0]) + coordinates[1] + j])
            print([coordinates[0] + j], [coordinates[1] + j])
            print(diag_list)
            j+=1
        except IndexError:
            break

    return True
"""
def check_win_diag(coordinates: list[int], player: str):   
    diag = []
    print(coordinates)
    coordinates[0] = coordinates[0] + len(board)
    i = 0
    while i < 4:
        try:
            if not coordinates[1] - i < 0:
                diag.append(board[coordinates[0] + i][coordinates[1] - i])
                print(diag)
                print(coordinates[0] + i, coordinates[1] - i)
            i+=1
            print()
        except IndexError:
            break
    i = 1
    while i < 4:
        try:
            if not coordinates[0] - i < 0:
                diag.insert(0, board[coordinates[0] - i][coordinates[1] + i])
                print(diag)
                print(coordinates[0] - i, coordinates[1] + i)
            i += 1
            print()
        except IndexError:
            break
        i +=1
    test_diag = []
    i=0
    while i < len(diag) - 1:
        if e == player and e == diag[i+1]:
            test_diag.append(e)
        elif e == player and e == diag[i-1] and e != diag[i+1]:
            test_diag.append(e)
            i+=1
    if len(test_diag) >=4:
        return True
    else:
        return False



def check_win_diag_2(coordinates: list[int], player: str):   
    diag = []
    print(coordinates)
    coordinates[0] = coordinates[0] + len(board)
    i = 0
    while i < 4:
        try:
            diag.append(board[coordinates[0] + i][coordinates[1] + i])
            print(diag)
            print(coordinates[0] + i, coordinates[1] + i)
            i+=1
            print()
        except IndexError:
            break
    i = 1
    while i < 4:
        try:
            if not coordinates[0] - i < 0 or coordinates[1] - i < 0:
                diag.insert(0, board[coordinates[0] - i][coordinates[1] - i])
                print(diag)
                print(coordinates[0] - i, coordinates[1] - i)
            i += 1
            print()
        except IndexError:
            break
        i +=1

    test_diag = []
    i=0
    while i < len(diag) - 1:
        if diag[i] == player and e == diag[i+1]:
            test_diag.append(diag[i])
        elif e == player and e == diag[i-1] and e != diag[i+1]:
            test_diag.append(e)
            i+=1
    if len(test_diag) >=4:
        return True
    else:
        return False


def check_win(coordinates: list[int], player: str) -> bool:
    conditions = [ 
       check_win_diag(coordinates, player),
       check_win_diag_2(coordinates, player)]
    if True in conditions:
        return True
    else: return False

def print_board():
    numbers = [
        "1️⃣",
        "2️⃣",
        "3️⃣",
        "4️⃣",
        "5️⃣",
        "6️⃣",
        "7️⃣",

     ]
    for num in numbers:
        print(num, end= "  ")
    print()
    for row in board:
        for e in row:
            print(e, end=' ')
        print()


def engine(player: str, player_1_username: str,  player_2_username: str):
    running = True
    turn = 1
    while running == True:
        print_board()
        print(f'turn #{turn}')
        print(f'{player} {player_2_username if turn % 2 == 0 else player_1_username}')
        print('Which column do you want to insert your thing (between 1 and 7)')
        selected_column = utils.get_int_in_range(1, 7)
        try:
            coordinates: list[int] = insert_into_col(selected_column, player)
            win = check_win(coordinates, player)
            if win:
                winner = player_1_username if turn % 2 != 0 else player_2_username
                print_board()
                print()
                print(f"{player} {winner} wins the game")
                break
            player = switch_player(player)
            turn +=1
            if turn == 42:
                print("It's a draw!")
                break
        except ColumnFull:
            print("the column is already full")
        except OutOfBoard:
            print("The column doesn't exist")

        


    
    
    

def main():
    
    player = '🔴'
    print('Welcome to connect four')
    print('Player 1 insert your username')
    player_1_username: str =  'test' # utils.get_string_in_range(2, 10)
    print('Player 2 insert your username')
    player_2_username: str =  'test2' # utils.get_string_in_range(2, 10)
    engine(player, player_1_username, player_2_username)
    pass



if __name__ == '__main__':
    main()
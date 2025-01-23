import sys
sys.path.append('../modules')
from modules import utils

class ColumnFull(IndexError):
    pass
class OutOfBoard(IndexError):
    pass

board: list[list[str]] = [
    [ '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵'],
    [ '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵'],
    [ '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵'],
    [ '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵'],
    [ '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵'],
    [ '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵',  '🔵'],
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
        
        
def check_win_down(coordinates: list[int], player: str):    
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
    
def check_win_left(coordinates: list[int], player: str):    
    retvalue = True
    try:
        for i in range(4):
            if board[coordinates[0]][coordinates[1] - i] == player:
                continue
            else:
                retvalue = False
                return retvalue
    except IndexError:
        retvalue = False
    finally:
        return retvalue

def check_win_left(coordinates: list[int], player: str):    
    retvalue = True
    try:
        for i in range(4):
            if board[coordinates[0]][coordinates[1] - i] == player:
                continue
            else:
                retvalue = False
                return retvalue
    except IndexError:
        retvalue = False
    finally:
        return retvalue

def check_win_right(coordinates: list[int], player: str):   
    retvalue = True
    try:
        for i in range(4):
            if board[coordinates[0]][coordinates[1] + i] == player:
                continue
            else:
                retvalue = False
                return retvalue
    except IndexError:
        retvalue = False
    finally:
        return retvalue
    
def check_win_down_left(coordinates: list[int], player: str):   
    retvalue = True
    try:
        for i in range(4):
            if board[coordinates[0]+i][coordinates[1] - i] == player:
                continue
            else:
                retvalue = False
                return retvalue
    except IndexError:
        retvalue = False
    finally:
        return retvalue
    
def check_win_down_right(coordinates: list[int], player: str):   
    retvalue = True
    try:
        for i in range(4):
            if board[coordinates[0]+i][coordinates[1] + i] == player:
                continue
            else:
                retvalue = False
                return retvalue
    except IndexError:
        retvalue = False
    finally:
        return retvalue
    
def check_win_up_right(coordinates: list[int], player: str):   
    retvalue = True
    try:
        for i in range(4):
            if board[coordinates[0] - i][coordinates[1] + i] == player:
                continue
            else:
                retvalue = False
                return retvalue
    except IndexError:
        retvalue = False
    finally:
        return retvalue
    
def check_win_up_left(coordinates: list[int], player: str):   
    retvalue = True
    try:
        for i in range(4):
            if board[coordinates[0] - i][coordinates[1] - i] == player:
                continue
            else:
                retvalue = False
                return retvalue
    except IndexError:
        retvalue = False
    finally:
        return retvalue

def check_win(coordinates: list[int], player: str) -> bool:
    conditions = [
        check_win_up_right(coordinates, player),
        check_win_right(coordinates, player),
        check_win_down_right(coordinates, player),
        check_win_down(coordinates, player),
        check_win_down_left(coordinates, player),
        check_win_left(coordinates, player),
        check_win_up_left(coordinates, player)]
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
    player_1_username: str = utils.get_string_in_range(2, 10)
    print('Player 2 insert your username')
    player_2_username: str = utils.get_string_in_range(2, 10)
    engine(player, player_1_username, player_2_username)
    pass



if __name__ == '__main__':
    main()
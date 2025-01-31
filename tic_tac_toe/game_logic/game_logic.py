from modules import utils  

from modules import utils
board = [[' ', ' ', ' ' ],
         [' ', ' ', ' ' ],
         [' ', ' ', ' ' ]]



def print_board():
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f"------------")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f"------------")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")

def switch_player(player: str) -> str:
    player = 'X' if player == 'O' else 'O'
    return player

def get_coordinates():
    while True:
        try:
            print("Select the row")
            row = utils.get_int_in_range(1, 3)
            print("Select the column")
            col = utils.get_int_in_range(1, 3)
            if board[row - 1][col - 1] != ' ':
                raise IndexError
        except IndexError:
            print("This cell is already taken, try again")
            print_board()
        else:    
            return (row - 1, col - 1)
    
def update_board(coordinates: tuple[int, int], player: str):
    row = coordinates[0]
    col = coordinates[1]
    board[row][col] = player


def check_win(player: str):
    # Same checks for win, returning True or False
    for row in board:
        if row == [player, player, player]:
            return True

    if [board[0][0], board[1][1], board[2][2]] == [player, player, player]:
        return True
    if [board[0][2], board[1][1], board[2][0]] == [player, player, player]:
        return True

    for col in range(3):
        if [board[0][col], board[1][col], board[2][col]] == [player, player, player]:
            return True

    return False


def engine():
    running = True
    player = 'X'
    turn = 0
    while running:
        print_board()
        print(f"{player}'s turn")
        coordinates = get_coordinates()
        update_board(coordinates, player)
        if check_win(player):
            print_board()
            print(f"{player} wins")
            running = False
            break
        player = switch_player(player)
        turn +=1
        if turn == 9:
            print_board()
            print("It's a draw")
            running = False

if __name__ == '__main__':
    engine()
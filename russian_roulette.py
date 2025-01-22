from random import shuffle, randint
import sys
sys.path.append('../modules')
from modules import utils

# Function to get a valid integer input
def get_int() -> int:
    while True:
        try: 
            retvalue: int = int(input("Please insert an integer number: ")) 
        except ValueError: 
            print("This is not an integer number")
        else:
            return retvalue

# Function to get an integer greater than or equal to a minimum value
def get_int_greater_or_equal_than(min_value: int) -> int:
    while True:
        try:
            retvalue: int = get_int()
            if retvalue < min_value:
                raise utils.TooSmall # Raise custom error if too small
        except utils.TooSmall:
            print(f"The integer number must be >= {min_value}")
        else:
            return retvalue

# Function to get an integer smaller than or equal to a maximum value
def get_int_smaller_or_equal_than(max_value: int) -> int:
    while True:
        try:
            retvalue: int = get_int()
            if retvalue > max_value:
                raise utils.TooLarge  # Raise custom error if too large
        except utils.TooLarge:
            print(f"The integer number must be <= {max_value}")
        else:
            return retvalue

# Function to get an integer within a specified range
def get_int_in_range(min_value: int, max_value: int) -> int:
    while True:
        try:
            retvalue: int = get_int_smaller_or_equal_than(max_value)
            if retvalue < min_value:
                raise utils.TooSmall  # Raise error if below range
        except utils.TooSmall:
            print(f"The integer number must be between {min_value} and {max_value}")
        else:
            return retvalue

# Function to get a string of specified length without spaces
def get_string_in_range(min_value: int, max_value: int) -> str:
    while True:
        try:
            retvalue: str = input()
            if " " in retvalue:  # Check for spaces
                raise utils.SpacesInString
            if len(retvalue) < min_value:  # Check minimum length
                raise utils.TooSmall
            if len(retvalue) > max_value:  # Check maximum length
                raise utils.TooLarge
        except utils.TooSmall:
            print(f"Insert at least {min_value} chars")
        except utils.TooLarge:
            print(f"Insert maximum {max_value} chars")
        except utils.SpacesInString:
            print("Spaces are not allowed")
        else:
            return retvalue

def get_bool() -> bool:
    yes_answers = ["1", "yes", "yep", "yeah", "y"]
    no_answers = ["", "0", "no", "nope", "nah", "n"]
    while True:
            try: 
                user_input = input().lower()
                if user_input not in yes_answers + no_answers:
                    raise ValueError
            except ValueError: 
                print("Invalid response.")
                print(f"To say yes type any of these: {yes_answers}")
                print(f"To say no type any of these: {no_answers}")

            else:
                if user_input in yes_answers:
                    retvalue = True
                else:
                    retvalue = False 

                return retvalue





def engine(revolver: list[bool], actual_turn: int, actual_player: str, index: int, player_turn: int, player_1: str, player_2: str):
    while revolver[index] == False:
        print(f"{actual_turn}. {actual_player}  click")
        index += 1
        actual_turn += 1
        player_turn = 1 if actual_player == player_2 else 2
        actual_player = player_1 if player_turn == 1 else player_2
    else:
        print(f"{actual_turn}. {actual_player}  BANG!")
        print(f"{actual_player} Dies :(")
        winner = player_1 if actual_player == player_2 else player_2
        print(f"{winner} Lives :)")



def main():
    min_username_lenght: int = 2
    max_username_lenght: int = 8

    print("Insert first player username: ")
    player_1: str = get_string_in_range(min_username_lenght, max_username_lenght)  # Get valid username for player 1

    print("Insert second player username: ")
    player_2: str = get_string_in_range(min_username_lenght, max_username_lenght)  # Get valid username for player 2
    print("Welcome players, let's play a game \nDo you know roussian roulette?")
    knows_game: bool = get_bool()
    print("Good") if knows_game == True else print("We decide the number of chambers and the number of bullets inside a revolver.\nWe load the revolver and spin the cylinder. Then each turn a player shoots the revolver. Last one alive wins.")

    print("How many chambers in the cylinder?")
    chambers = get_int_greater_or_equal_than(1)
    print("How many bullets?")
    bullets = get_int_in_range(0, chambers)
    if bullets == 0:
         print("You chose peace, congrats")
         return
     # Create a list with bullets (True) and empty chambers (False)
    revolver = [True] * bullets + [False] * (chambers - bullets)
    shuffle(revolver)

    actual_turn: int = 1
    print("Let's see who starts")
    player_turn: int = randint(1, 2)

    if player_turn == 1:
        actual_player = player_1
    else:
        actual_player = player_2

    print(f"{actual_player}'s gonna shoot first")

    engine(revolver, actual_turn, actual_player, 0, player_turn, player_1, player_2)

if __name__ == "__main__":
    main()

from random import randint

# Custom exception classes for specific error handling
class TooLarge(ValueError):
    pass

class TooSmall(ValueError):
    pass

class SpacesInString(ValueError):
    pass

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
                raise TooSmall  # Raise custom error if too small
        except TooSmall:
            print(f"The integer number must be >= {min_value}")
        else:
            return retvalue

# Function to get an integer smaller than or equal to a maximum value
def get_int_smaller_or_equal_than(max_value: int) -> int:
    while True:
        try:
            retvalue: int = get_int()
            if retvalue > max_value:
                raise TooLarge  # Raise custom error if too large
        except TooLarge:
            print(f"The integer number must be <= {max_value}")
        else:
            return retvalue

# Function to get an integer within a specified range
def get_int_in_range(min_value: int, max_value: int) -> int:
    while True:
        try:
            retvalue: int = get_int_smaller_or_equal_than(max_value)
            if retvalue < min_value:
                raise TooSmall  # Raise error if below range
        except TooSmall:
            print(f"The integer number must be between {min_value} and {max_value}")
        else:
            return retvalue

# Function to get a string of specified length without spaces
def get_string_in_range(min_value: int, max_value: int) -> str:
    while True:
        try:
            retvalue: str = input()
            if " " in retvalue:  # Check for spaces
                raise SpacesInString
            if len(retvalue) < min_value:  # Check minimum length
                raise TooSmall
            if len(retvalue) > max_value:  # Check maximum length
                raise TooLarge
        except TooSmall:
            print(f"Insert at least {min_value} chars")
        except TooLarge:
            print(f"Insert maximum {max_value} chars")
        except SpacesInString:
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
                print(f"To play again type any of these: {yes_answers}")
                print(f"To stop plaing again type any of these: {no_answers}")

            else:
                if user_input in yes_answers:
                    retvalue = True
                else:
                    retvalue = False 

                return retvalue

# Main game logic
def main() -> None:
    print("Insert first player username: ")
    player_1: str = get_string_in_range(2, 10)  # Get valid username for player 1

    print("Insert second player username: ")
    player_2: str = get_string_in_range(2, 10)  # Get valid username for player 2

    is_playing: int = 1
    while is_playing == 1:

        print("Insert matchsticks' number on the table: ")
        starting_matches: int = get_int_greater_or_equal_than(2)  # Ensure at least 2 matchsticks
        remaining_matchsticks: int = starting_matches
        print("Insert maximum amount of pickups per round: ")
        max_pickups: int = get_int_in_range(1, remaining_matchsticks - 1)  # Max pickups less than matchsticks


        print("Let's see who starts")
        player_turn: int = randint(1, 2)  # Randomly decide who starts (1 or 2)

        # Main game loop
        while remaining_matchsticks > 1:
            # Adjust max pickups if matchsticks are low
            if remaining_matchsticks <= max_pickups:
                max_pickups = remaining_matchsticks - 1

            # Determine current player
            player_current: str = player_2 if player_turn == 2 else player_1
            
            print(f"{player_current}'s turn, there are {remaining_matchsticks} matchsticks on the table")
            print("How many matchsticks do you pick up?")
            remaining_matchsticks -= get_int_in_range(1, max_pickups)  # Subtract matchsticks

            # Switch player turn
            player_turn = 1 if player_turn == 2 else 2

        # Game over logic
        player_current = player_1 if player_turn == 2 else player_2 #Switch current player to display the winner. Otherwise it would have displayed the loser
        print(f"Game ends because there is only 1 matchstick on the table. {player_current} wins")
        print("Want to play again [Y/N]")
        is_playing = get_bool()
# Run the game
if __name__ == "__main__":
    main()

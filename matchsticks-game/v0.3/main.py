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
def get_string_in_range(min_lenght: int, max_lenght: int) -> str:
    while True:
        try:
            retvalue: str = input()
            if " " in retvalue:  # Check for spaces
                raise SpacesInString
            if len(retvalue) < min_lenght:  # Check minimum length
                raise TooSmall
            if len(retvalue) > max_lenght:  # Check maximum length
                raise TooLarge
        except TooSmall:
            print(f"Insert at least {min_lenght} chars")
        except TooLarge:
            print(f"Insert maximum {max_lenght} chars")
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
                print(f"To say yes type any of these: {yes_answers}")
                print(f"To say no type any of these: {no_answers}")

            else:
                if user_input in yes_answers:
                    retvalue = True
                else:
                    retvalue = False 

                return retvalue

def winner_printer(player: str) -> None: #A function for this functionality because in the future i may want to write this in a file and not only on the console
    print(f"Game ends because there is only 1 matchstick on the table. {player} wins")

def win_count_printer(player_1: str, player_1_win_counter: int, player_2: str, player_2_win_counter: int): #A function for this functionality because in the future i may want to write this in a file and not only on the console
    print(f"Win count:\n{player_1}: {player_1_win_counter}\n{player_2}: {player_2_win_counter}")

def engine(remaining_matchsticks: int, max_pickups: int, player_1: str, player_2: str) ->str: # type: ignore

        actual_turn: int = 1
        print("Let's see who starts")
        player_turn: int = randint(1, 2)  # Randomly decide who starts (1 or 2)
        print(f"Starting matches: {remaining_matchsticks}, maximum amount of pickup: {max_pickups}")
        if player_turn == 1:
            starter = player_1
        else:
            starter = player_2
        print(f"{starter} Is the first to play")

        # Main game loop
        while remaining_matchsticks > 1:
            # Adjust max pickups if matchsticks are low
            endgame_max_pickups = max_pickups
            if remaining_matchsticks <= endgame_max_pickups:
                endgame_max_pickups = remaining_matchsticks - 1

            # Determine current player
            player_current: str = player_2 if player_turn == 2 else player_1
            print(f"turn {actual_turn}")
            if actual_turn != 1: 
                print(f"{player_current}'s turn, there are {remaining_matchsticks} matchsticks on the table, you can pick at most {endgame_max_pickups} matchsticks")
            print("How many matchsticks do you pick up?")
            remaining_matchsticks -= get_int_in_range(1, endgame_max_pickups)  # Subtract matchsticks

            # Switch player turn and increment actual turn
            player_turn = 1 if player_turn == 2 else 2
            actual_turn += 1

        # Game over logic
        player_current = player_1 if player_turn == 2 else player_2 #Switch current player to display the winner. Otherwise it would have displayed the loser
        return player_current
    


# Main game logic
def main() -> None:
    min_username_lenght: int = 2
    max_username_lenght: int = 8

    print("Insert first player username: ")
    player_1: str = get_string_in_range(min_username_lenght, max_username_lenght)  # Get valid username for player 1

    print("Insert second player username: ")
    player_2: str = get_string_in_range(min_username_lenght, max_username_lenght)  # Get valid username for player 2

    print(
f"""
Welcome to the game {player_1} and {player_2}.
          
The game works like this:

You choose the starting number of matchsticks on the table.
You choose the maximum ammount of matchsticks a player can pick in its turn.
We then flip a coin to decide who starts.

The player picks up some matchsticks between 1 and the maximum ammount you chose before.
Then it's the other player turn, it goes on until there is more than 1 matchstick on the table
The player who leaves 1 matchstick on the table wins.
          
You can then choose if you want to play again or not and if you want to change the 
starting number of matchsticks and the maximum ammount of pickup or not.

The game keeps track of all the wins for each player and displays them at the end of every match          
"""
)

    game_condition: bool = True

    player_1_win_counter: int = 0
    player_2_win_counter: int = 0
    is_playing: int = 1
    while is_playing == 1:
        while game_condition == True:
            print("Insert matchsticks' number on the table: ")
            starting_matches: int = get_int_greater_or_equal_than(2)  # Ensure at least 2 matchsticks
            remaining_matchsticks: int = starting_matches
            print("Insert maximum amount of pickups per round: ")
            max_pickups: int = get_int_in_range(1, remaining_matchsticks - 1)
            game_condition = False

        winner: str = engine(remaining_matchsticks, max_pickups, player_1, player_2)  # type: ignore
        winner_printer(winner)
        if winner == player_1:
            player_1_win_counter += 1
        else:
            player_2_win_counter += 1
        print(f"Win count:\n{player_1}: {player_1_win_counter}\n{player_2}: {player_2_win_counter}")
        print("Want to play again? [Y/N]")
        is_playing = get_bool()
        
        if is_playing == True:
            print("Do you want to change the game starting conditions? [Y/N]")
            game_condition=get_bool()
    
# Run the game
if __name__ == "__main__":
    main()

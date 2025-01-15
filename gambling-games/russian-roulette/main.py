from random import shuffle, randint

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
                print(f"To say yes type any of these: {yes_answers}")
                print(f"To say no type any of these: {no_answers}")

            else:
                if user_input in yes_answers:
                    retvalue = True
                else:
                    retvalue = False 

                return retvalue

                 

def start():
    print("Welcome user, let's play a game \nDo you know roussian roulette?")
    knows_game: bool = get_bool()
    print("Good") if knows_game == True else print("We decide the number of chambers and the number of bullets inside a revolver.\nWe load the revolver and spin the cylinder. Then each turn a player shoots the revolver. Last one alive wins.")

    print("How many chambers?")
    chambers = get_int_greater_or_equal_than(1)
    print("How many bullets?")
    bullets = get_int_in_range(0, chambers)
     # Create a list with bullets (True) and empty chambers (False)
    if bullets == 0:
         print("You chose peace, congrats")
         return
    revolver = [True] * bullets + [False] * (chambers - bullets)
    shuffle(revolver)
    print(revolver)
     
def game():
    



def main():
    start()

if __name__ == "__main__":
    main()

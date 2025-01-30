# Custom exception classes for specific error handling
class TooLarge(ValueError):
    pass

class TooSmall(ValueError):
    pass

class SpacesInString(ValueError):
    pass

class NotValidAnswer(ValueError):
    pass 

def get_int() -> int:
    while True:
        try: 
            retvalue: int = int(input("Please insert an integer number: ")) 
        except ValueError: 
            print("This is not an integer number")
        else:
            return retvalue
        
def get_float() -> float:
    while True:
        try: 
            retvalue: float = float(input("Please insert a number: ")) 
        except ValueError: 
            print("This is not a number")
        else:
            return retvalue

def get_float_not(banned_value: float | None) -> float:
    while True:
        try: 
            retvalue: float = get_float()
            if retvalue == banned_value:
                raise ValueError  
        except ValueError:
            print(f"{banned_value} is not an accepted value")
        else:
            return retvalue
        
def get_many_floats() -> list[float]:
    retvalue: list[float] = []
    while True:
        try:
            user_input = (input("Insert a number to continue or leave blank to stop:"))
            if user_input == '':
                break
            number: float = float(user_input)
        except ValueError: 
            print("This is not a number")
        else:
            retvalue.append(number)
    return retvalue

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
        
def get_string_accepted_values(accepted_values: list[str]):
    while True:
        retvalue: str = input().strip()
        for char in retvalue: 
            try:
                if not char in accepted_values:
                    raise NotValidAnswer
            except NotValidAnswer:
                print(f"Only accepted input are made of: {accepted_values}")
                retvalue: str = input()
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
            
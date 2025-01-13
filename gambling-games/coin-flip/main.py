import random

"""
class PositiveIntegerError(ValueError):
    pass
class NumberTooLargeError(ValueError):
    pass
def get_valid_input(prompt, max_num, error_generic, error_positive, error_max): #ensure the input is an integer greater than 0
    while True:
        try:
            faces_number = int(input(prompt))
            if faces_number <= 0:
                raise PositiveIntegerError
            if faces_number > max_num:
                raise NumberTooLargeError
            return faces_number
        except PositiveIntegerError:
            print (error_positive)
        except NumberTooLargeError:
            print (error_max, max_num) 
        except ValueError:
            print (error_generic)
"""

#return the input from the user
def input_reader() -> int:
    retvalue: int = int(input("Inserisci il numero di facce: "))
    return retvalue 

#return random int between 1 and max_value (including)
def work(max_value: int) -> int: 
    retvalue: int = random.randint(1, max_value)
    return retvalue

def output_writer(value: int) -> None:
    print("The result is:", value)

def main():
    """ 
    faces_number: int = get_valid_input(
                    "Insert the number of faces: ", #prompt
                    40, #maximum number of faces
                    "Please, insert an integer number", #error message if a user isert a float or string or nothing
                    "Please, the number cannot have less than 1 face", #error message if a user isert an int smaller than 1
                    "Please, the number cannot be greater than") #error message if a user isert an int greater than maximum number of faces
    """
    faces_number = input_reader()

    result: int = work(faces_number)
    
    output_writer(result)

if __name__ == "__main__":
    main()
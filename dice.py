import random
import sys
sys.path.append('../modules')
from modules import utils

def input_reader() -> int:
    retvalue: int = utils.get_int_greater_or_equal_than(2)
    return retvalue 

def work(max_value: int) -> int: 
    retvalue: int = random.randint(1, max_value)
    return retvalue

def output_writer(value: int) -> None:
    print("The result is:", value)

def main():
    faces_number = input_reader()
    result: int = work(faces_number)
    output_writer(result)

if __name__ == "__main__":
    main()
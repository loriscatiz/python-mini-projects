import sys
sys.path.append('../modules')
from modules import utils

operators =  ['+', '-', '/', '*']

def add_all(*args: float) -> float:
    partial_result = 0
    for element in args:
        partial_result = add(partial_result, element)
    retvalue = partial_result
    return retvalue

def subtract_all(*args: float) -> float:
    partial_result = 0
    for element in args:
        partial_result = subtract(partial_result, element)
    retvalue = partial_result
    return retvalue

def multiply_all(*args: float) -> float:
    partial_result = 1
    for element in args:
        partial_result = multiply(partial_result, element)
    retvalue = partial_result
    return retvalue

def divide_all(*args: float) -> float:
    partial_result = args[0]**2
    while True:
        for element in args:
            partial_result = divide(partial_result, element)   
        return partial_result



def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    while True:
        try:
            retvalue = a / b
        except ZeroDivisionError:
            print("You can't divide by 0, please insert a valid dividend")
            b = utils.get_float()
        else:
            return retvalue
        

def get_operator(operators: list[str]) -> str:
    while True:
        try:
            retvalue = input()
            if retvalue not in operators: raise utils.NotValidAnswer
        except utils.NotValidAnswer:
            print(f'{retvalue} is not a valid operator') # type: ignore
            print(f'The valid operators are: {operators}') 
        else:
            return retvalue
def calculate(first_num: float, operator: str, second_num: float ) -> float:  
    match operator:
        case '+':
            result = add(first_num, second_num)
        case '-':
            result = subtract(first_num, second_num)
        case '/':
            result = divide(first_num, second_num)
        case '*':
            result = multiply(first_num, second_num)
        case _:
            result = 'An unexpected error occured'
    return result # type: ignore
    
def calculate_all(operator: str ,*operands: float):
    match operator:
        case '+':
            result = add_all(*operands)
        case '-':
            result = subtract_all(*operands)
        case '/':
            result = divide_all(*operands)
        case '*':
            result = multiply_all(*operands)
        case _:
            result = 'An unexpected error occured'
    return result 

def main() -> None:


    print('Select an operation to make: ')
    test = get_operator(operators)
    
    print('Select numbers to operate:')
    numbers: list[float] = utils.get_many_floats()

    result = calculate_all(test, *numbers) 
    

    print(f'The result the {test} operation for theese numbers {numbers} is {result}')



if __name__ == '__main__':
    main()
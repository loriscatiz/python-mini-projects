"""
Write a program that asks the users for two number and 
tells the user which is greater 
"""


def get_valid_input(prompt: str): #Return a float number
    while True:
        try: retvalue = float(input(prompt))
        except ValueError: print("Please, insert a valid value")
        else: return retvalue

def main():

    a = 0
    b = ""
    if a:
        print("a")
    if b:
        print("b")
    """

    x1 = get_valid_input("Insert first number: ")
    x2 = get_valid_input("Insert second number: ")

    if x1 > x2: 
        print(x1, "is greater than", x2)
    elif x1 < x2: 
        print(x2, "is greater than", x1)
    else: 
        print(x1, "and", x2, "are equal")


        """
"""     x1 = get_valid_input("Insert first number: ")
    x2 = get_valid_input("Insert second number: ")
    x3 = get_valid_input("Insert third number")

    numbers: list[float] = [x1, x2, x3]
    max_num: float = (max(numbers)) 
    
    for i, num in enumerate(numbers):
        if num == max_num:
            print(f"{i+1} number, {num}")
 """

if __name__ == "__main__":
    main()
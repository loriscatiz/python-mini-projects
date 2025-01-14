"""
Matchstick game
Players number: 2
Matchsticks number: variable
Players' names: variables
Max number of pickups: variable 
Win condition: the player leaving the last matchstick on the table wins.
"""

# get_items_number function must ask the user the
# number of matchsticks to start the game and return this value
# 
# potential problems:
# 1) Number must be an integer
# 2) The integer must be greater than 1

def get_items_number() -> int:

    retvalue: int = 0 #We force an initial error 
    while retvalue <= 1:

        try: #We insert code that may result in error inside the try block
            retvalue = int(input("Please insert an integer nummber > 1: "))
        except: #We insert code that executes if there is an error inside the except block
            print("Error")

        if retvalue <= 1: #Print feedback to the user if retvalue is less than or equal to 1
            print("Number must be > 1")

    return retvalue    

#item_picker function must ask the user an integer number x respecting the following conditions:
# x > 1 and x <= max_value

def item_picker(max_value: int) -> int:
    retvalue : int = max_value + 1

    while retvalue > max_value:
        retvalue = get_items_number()
        if retvalue > max_value:
            print("Number must be <", max_value)
    return retvalue

def main() -> None:
    #Ask the number of matchsticks on the table
    print("Insert matchsticks' number on the table: ")
    remaining_items = get_items_number()

    #Set the max number of pickups
    print("Insert matchstick number of max pickups: ")
    max_pickup = item_picker(remaining_items - 1)

    print(f"Matchsticks number: {remaining_items} - Max pickup: {max_pickup}")

if __name__ == "__main__":
    main()
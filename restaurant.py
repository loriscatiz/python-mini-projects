"""
Ask the user how many people seated at the table and ask the how much is the total bill
It should return how much each person should pay
"""

class NotPositiveNum(Exception):
    pass

def get_people() -> int:
    while True:
        try:
            people: int = int(input("How many people: "))
            if people <= 0:
                raise NotPositiveNum
        except ValueError:
            print("Please insert an integer number.")
        except NotPositiveNum:
            print ("Insert a positive number")

        else:
            return people

def get_bill() -> float:
    while True:
        try:
            bill: float = float(input("How much is the total: "))
            if bill <= 0:
                raise NotPositiveNum 
        except ValueError:
            print("Please insert a float number.")
        except NotPositiveNum:
            print ("Insert a positive number")
        else:
            return bill

def main():
    people = get_people()
    bill = get_bill()
    share = bill / people
    print(f"There are {people} people, the total is {bill}. Each person's share is {share:.2f}")

if __name__ == '__main__':
    main()
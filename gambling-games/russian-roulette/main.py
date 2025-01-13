import random

def get_int(prompt) -> int:
    while True:
        try:
            retvalue = int(input(prompt))
            return retvalue
        except ValueError:
            print("That's not an int, please try again")

def get_int_max(prompt: str, max_num: int):
        while True:
            try:
                retvalue = get_int(prompt)
                if retvalue > max_num:
                    raise ValueError
                return retvalue
            except ValueError:
                print ("Write a number lower than", max_num)

def get_int_min(prompt, min_num):
        while True:
            try:
                retvalue = get_int(prompt)
                if retvalue < min_num:
                    raise ValueError
                return retvalue
            except ValueError:
                print ("Write a number greater than", min_num)

def get_int_max_min(max_num, min_num):
     while True:
            try:
                retvalue = get_int_max(f"insert a number smaller than {max_num}" + f" and bigger than {min_num} ", max_num)
                if not (retvalue <= max_num and retvalue >= min_num): 
                    raise ValueError
                return retvalue
            except ValueError:
                 print ("not in between", min_num, max_num)
                 

def start():
    print("Welcome user, let's play a game \nDo you know roussian roulette?")
    chambers = get_int_min("How many chambers?\n", 1)
    print("How many bullets?")
    bullets = get_int_max_min(chambers, 0)
     # Create a list with bullets (True) and empty chambers (False)
    if bullets == 0:
         print("You chose peace, congrats")
         return
    revolver = [True] * bullets + [False] * (chambers - bullets)
    random.shuffle(revolver)
    turn: int = 1
    print("Here we go, let's see who starts...")
     
def game():
    pass



def main():
    pass
    # num = get_int_max_min( 6, 1)
    # print(num, "is a valid value")
    start()
    

if __name__ == "__main__":
    main()
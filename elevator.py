import sys
sys.path.append('../modules')
from modules import utils

class ElevetorEnded(ValueError):
    pass

def move(elevator_min_floor: int, elevator_max_floor: int, current_floor: int):
    accepted_values = ['^', 'v', '']
    moving_command: str = utils.get_string_accepted_values(accepted_values)
    for char in moving_command:
        if char == '^':
            try:
                if current_floor + 1 > elevator_max_floor:
                    raise ElevetorEnded
            except ElevetorEnded:
                print('You reached the highest floor')
            else:
                current_floor +=1
        if char == 'v':
            try:
                if current_floor < elevator_min_floor:
                    raise ElevetorEnded
            except ElevetorEnded:
                print('You reached the lowest floor')
            else:
                current_floor -=1
        print(f"You are at floor {current_floor}")
    print(f"You ended up at floor {current_floor}")

def main():
    print('How many floors are there?')
    floors = utils.get_int_greater_or_equal_than(1)
    print("How many floors underground?")
    min_floor = - utils.get_int_in_range(0, floors -1)
    max_floor =   floors + min_floor -1
    print('What is the current floor?')
    current_floor = utils.get_int_in_range(min_floor, max_floor)

    print(f"You are at floor {current_floor}")
    print('To move, input a string made of "^" and "v" "^" goes up, "v" goes down ')
    move(min_floor, max_floor, current_floor)

if __name__ == '__main__':
    main()

import sys
sys.path.append('../modules')
from modules import utils


def main():
    num_list: list[int] = []
    while True:
        print("Type an integer to add an istogram of that lenght. Insert '-1' to get the result")
        user_input = utils.get_int_greater_or_equal_than(-1)
        if user_input == -1:
            break
        num_list.append(user_input)

    for n in num_list:
        isto_lenght = n
        isto_bar: str = n * '*'
        print(isto_lenght, isto_bar) 

if __name__ == '__main__':
    main()
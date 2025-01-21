import random
import sys
sys.path.append('../modules')
from modules import utils


min_max_guess: dict[str, int] = {'min': 0, 'max': 100}
winning_number: int = random.randint(min_max_guess['min'], min_max_guess['max'])

def main() -> None:
    max_tries: int = 5
    current_try: int = 1

    print(f"""
The game is to guess a number between {min_max_guess['min']} and {min_max_guess['max']}
After each try, you'll get an hint ('The winning number is higher or lower')
You have maximum {max_tries} tries. Let's play
""")
    utils.test()

    while current_try <= max_tries:
        user_guess = utils.get_int_in_range(min_max_guess['min'], min_max_guess['max'])
        if not user_guess == winning_number: 
            print(f'{current_try}. Your guess was {user_guess}. The winner number is {'lower' if winning_number < user_guess else 'higher'}')
            if current_try == 5:
                print('You lose :(')
                print(f'The winning number was {winning_number}')
            else:
                print('Try again ;)')
            current_try +=1
        else:
            print(f'{current_try}. You win!!! Your guess was correct :)')
            

if __name__ == '__main__':
    main()

""" 
user_guess: int = -1
tries: int = 1
while user_guess < 0 or user_guess > 100:
    while tries <= 5:
        user_guess = int(input(f'{tries} try. Guess the number between 0 and 100\n'))
        tries += 1
        if user_guess == winning_number:
            break
        else:
            user_guess = -1
            continue
    if user_guess == winning_number:
        print("You win!")
        break
    print("I'm sorry, you lose")
    break


 """


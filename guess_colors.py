import random

color_pool = [
    'red',
    'blue',
    'green',
    'yellow',
    'purple',
    'orange',
    'pink',
    'brown',
    'gray',
    'white'
]

replay_pool = ['yes', 'no', 'y', 'n']

max_turns = 4

def print_combination(combination: list[str]):
    for e in combination:
        print(e, end=" ")
        print()

def get_guessed_colors(winning_colors: list[str]):
    guessed_colors: list[str] = []
    i=0
    while i < (len(winning_colors)):
        color = ''
        while color not in color_pool:
            color = input(f'{i+1}. Guess: ').replace(" ", "").lower()
            if color in guessed_colors:
                print(f"You already picked {color}")
                continue
            if color not in color_pool:
                print(f"{color} not in the pool")
                print(f"The color pool is {color_pool}")
                continue
            guessed_colors.append(color)
            i+=1
    return guessed_colors
        
def check_win(winning_colors: list[str], guessed_colors: list[str]):
    if guessed_colors == winning_colors:
        print("You win")
        return True
    
def give_hints(winning_colors: list[str], guessed_colors: list[str]):
    colors_in_place = 0
    colors_not_in_place = 0
    for color in guessed_colors:
        if color in winning_colors and guessed_colors.index(color) == winning_colors.index(color):
            colors_in_place += 1
        elif color in winning_colors and guessed_colors.index(color) != winning_colors.index(color):
            colors_not_in_place += 1
    print("Your guess was: \n")
    print_combination(guessed_colors)
    print(f"You guessed {colors_in_place} correct in the correct position")
    print(f"You guessed {colors_not_in_place} correct in the wrong position")

def engine(max_turns: int):
    winning_colors = random.sample(color_pool, 4)
    print(f"Guess the {len(winning_colors)} colors in order")
    current_turn = 1
    while current_turn <= max_turns:
        print(f"{current_turn} Try")
        guessed_colors = get_guessed_colors(winning_colors)
        if check_win(winning_colors, guessed_colors):
            break
        if current_turn == max_turns:
            print(f"You lose, the correct combination was: ")
            print_combination(winning_colors)
            break
        else:
            current_turn +=1
            give_hints(winning_colors, guessed_colors)

def replay():
    again = ''
    while again not in replay_pool:
        again = input()
        if again not in replay_pool:
            print(f'The answer must be one of these: ')
            print_combination(replay_pool)
            continue
        if again == 'y' or again == 'yes':
            return True
        return False
 
def main():
    running = True
    while running == True:
        engine(max_turns)
        print("Do you wanna play again?")
        running = replay()

if __name__ == '__main__':
    main()
import random

def create_and_print_dictionaries():
    squares_and_cubes: dict[int, list[int]] = {}
    for i in range(1, 21):
        squares_and_cubes.update({i: [i**2, i**3]})
    print(squares_and_cubes)

def not_divisible_by_five_and_seven():
    num_pool: list[int] = []
    i=0
    while i < 100:
        num = random.randint(1, 200)
        #if the modulo operator returns 0 for both the num is divisible by both -> the condition is False, it doesn't append num
        if num % 5 and num % 7: 
            num_pool.append(num)
        i+=1
    print(num_pool)
    print(f"{100 - len(num_pool)} numbers removed")


def main():
#    create_and_print_dictionaries()
    not_divisible_by_five_and_seven()
    

if __name__ == '__main__':
    main()

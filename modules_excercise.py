import random

lista: list[int] = [1, 4, 10, 5]
random.shuffle(lista)
print(lista)


def flip() -> str:
    flip: int = random.randint(0, 1)
    if flip == 0:
        return "HEAD!"
    return "TAILS!"

def user_choice() -> str:
    print('Heads or Tails?')
    user_input: str = ''
    while user_input.lower() not in ['heads', 'h', 'tails', 't']:
        return input()

def main() -> None:
    user_choice()
    print(flip())
    
main()
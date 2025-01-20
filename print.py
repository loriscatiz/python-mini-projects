output: str = ''
while True:
    user_input: str = input("Insert something: ")
    output += user_input
    if user_input == '': break
    print(output, end = '->')

list = ['a', 'b', 'c']

e = list.pop()

print(e)
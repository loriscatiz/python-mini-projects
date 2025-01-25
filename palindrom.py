def check_palindrome(string: str):
    for i in range(len(string) // 2):
        j = len(string) - 1 - i
        if string[i] != string[j]:
            return False
    return True

user_input = input("Insert a string to check if it's a palindrome: \n")
if check_palindrome(user_input):
    print(f'The string \'{user_input}\' is palindrome')
else:
    print(f'The string \'{user_input}\' is not palindrome')
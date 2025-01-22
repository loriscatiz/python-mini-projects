def count_chars(arg: str):
    retvalue: dict[str, int] = {}
    for char in arg:
        if char in retvalue:
            retvalue[char] += 1
        else:
            retvalue[char] = 1
    return retvalue

def main() -> None:
    print("Write a string, i'll tell you how many times each character appears in that string")
    user_input = input()
    occurrences = count_chars(user_input)
    print(occurrences)

if __name__ == '__main__':
    main()
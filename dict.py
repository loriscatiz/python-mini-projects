def count_chars(arg: str):
    retvalue: dict[str, int] = {}
    for char in arg:
        if char in retvalue:
            retvalue.update(char, retvalue[char])
        else:
            retvalue[char] = 1
    return retvalue

def main() -> None:
    print(count_chars('ciao come stai?'))

if __name__ == '__main__':
    main()
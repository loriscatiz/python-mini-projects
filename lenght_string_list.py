def lenght_elements(start: list[str]) -> list[int]:
    retvalue: list[int] =[]
    for s in start:
        retvalue.append(len(s))
    return retvalue

def lenght_elements_v2(start: list[str]) -> list[int]:
    return list(map(len, start))

def main():
    print("Write a string, and I'll tell you the lengths of each word (including punctuation attached to it).")
    user_input: str = input()
    strings = user_input.split()
    print(f"Words:\n{strings}")
    print(f"manual function:\n{lenght_elements(strings)}")
    print(f"map function:\n{lenght_elements_v2(strings)}")

if __name__ == '__main__':
    main()
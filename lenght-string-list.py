def lenght_elements(start: list[str]) -> list[int]:
    retvalue: list[int] =[]
    for s in start:
        retvalue.append(len(s))
    return retvalue

def lenght_elements_v2(start: list[str]) -> list[int]:
    return list(map(len, start))

def len_str(string: str) -> int:
    i: int = 0
    while True:
        try:
            if string[i]:
                i += 1
        except IndexError:
            break
    return i

    

def main():
    strings: list[str] = ['ciao', 'come', 'va', '?', '', '9']
    print('manual function:', lenght_elements(strings))
    print('map function:', lenght_elements_v2(strings))

    test: str = 'ciao'
    print(len_str(test))

if __name__ == '__main__':
    main()
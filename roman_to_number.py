def romanToInt(s: str) -> int:
    values: dict[str, int] = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    retvalue = 0
    for i in range(len(s) - 1):
        if values[s[i]] >= values[s[i+1]]:
            retvalue += values[s[i]]
        else:
            retvalue -= values[s[i]]
    retvalue += values[s[-1]]
    return retvalue

print(romanToInt('IV'))
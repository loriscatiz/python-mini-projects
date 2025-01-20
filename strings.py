string: str = 'hello world!'

print(f'a[0]: {string[0]}')
print(f'a.capitalize(): {string.capitalize()}')
print(f'a.upper: {string.upper()}')
print(f'a.lower: {string.lower()}')

list1 = [1, 2]
list2 = list1.copy()
list1[0] = 0
print(list2)
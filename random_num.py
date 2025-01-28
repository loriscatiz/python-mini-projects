import random
import sorting_algorithms

num_list: list[int] = []
list_lenght = 90000
for i in range(list_lenght):
    num_list.append(random.randint(-999999, 999999))

num_list = sorting_algorithms.merge_sort(num_list) # type: ignore
max_num = num_list[list_lenght-1]
min_num = num_list[0]

even_nums = 0
odd_nums = 0
total = 0
for i in range(list_lenght):
    if num_list[i] % 2 == 0:
        even_nums += 1 
    else:
        odd_nums+=1
    total +=num_list[i]

average = total / list_lenght

if list_lenght % 2 == 0:
    median = (num_list[list_lenght // 2 - 1] + num_list[list_lenght // 2]) / 2
else:
    median = num_list[list_lenght // 2]


print(f"List: {num_list}")
print(f"Max: {max_num}")
print(f"Min: {min_num}")
print(f"Average: {average}")
print(f"Odd nums: {odd_nums}")
print(f"Even nums: {even_nums}")
print(f"Median: {median}")
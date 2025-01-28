import random
    
array: list[float] = []
for i in range(10):
    array.append(random.randint(0, 101))

def bubble_sort(array: list[float]):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                swapper = array[j]
                array[j] = array[j+1]
                array[j+1] = swapper
    return array

def selection_sort(array: list[float]):
    for i in range(len(array)):
        min_value = array[i]
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < min_value:
                min_value = array[j]
                min_index = j 
        temp = array[i] 
        array[min_index] = temp
        array[i] = min_value
    return array

def insertion_sort(array: list[float]):
    for i in range (1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0:
            if array[j] >= temp:
                array[j+1] = array[j]
                j-=1
            else:
                break
        array[j + 1] = temp
    return array

def merge_sort(array: list[float]) -> list[float]:
    if len(array) <= 1:
        return array
    left = array[:len(array)//2]
    right = array[len(array)//2:len(array)]
    sorted_left: list[float] = merge_sort(left)
    sorted_right: list[float] = merge_sort(right)
    return merge(sorted_left, sorted_right)

def merge(left: list[float], right: list[float]) -> list[float]:
    merged_array: list[float] = []
    i = 0
    j = 0
    while i < (len(left)) and j < len(right):
        if left[i] < right[j]:
            merged_array.append(left[i])
            i+=1
        else:
            merged_array.append(right[j])
            j+=1
    if i == len(left):
        merged_array.extend(right[j:])
    if j == len(right):
        merged_array.extend(left[i:])
    return merged_array


# selection_sort(array)
# insertion_sort(array)


def main():
    merge_sort(array)

if __name__ == '__main__':
    main()
array: list[float] = [ 15, 9, -4, 0.3, 3.5]

def bubble_sort(array: list[float]):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                swapper = array[j]
                array[j] = array[j+1]
                array[j+1] = swapper

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



# bubble_sort(array)
# selection_sort(array)
insertion_sort(array)
print(array)

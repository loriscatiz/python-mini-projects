not_bubbled: list[float] = [0.3, 15,9, 3.5, 6.1, 8, 61, -0.45]


for i in range(len(not_bubbled) - 1):
    for j in range(len(not_bubbled) - i - 1):
        print(not_bubbled[j])
        if not_bubbled[j] > not_bubbled[j+1]:
            swapper = not_bubbled[j]
            not_bubbled[j] = not_bubbled[j+1]
            not_bubbled[j+1] = swapper


print(not_bubbled)

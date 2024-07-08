def sort(array):
    for i in range(len(array) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array

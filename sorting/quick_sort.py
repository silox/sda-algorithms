def quicksort_additional_memory(array):
    # Pekna implementacia dobra na pochopenie algoritmu, no vyuziva pamat navyse
    if len(array) <= 1:
        return array

    pivot = array.pop()
    low_elements, equal_elements, high_elements = [], [pivot], []
    for item in array:
        if item == pivot:
            equal_elements.append(item)
        elif item > pivot:
            high_elements.append(item)
        else:
            low_elements.append(item)

    return quicksort_additional_memory(low_elements) + equal_elements + quicksort_additional_memory(high_elements)


def partition(array, left, right):
    pivot = array[right]
    for i in range(left, right):
        if array[i] <= pivot:
            array[i], array[left] = array[left], array[i]
            left += 1

    array[left], array[right] = array[right], array[left]
    return left


def _quicksort(array, left, right):
    if left < right:
        pivot_idx = partition(array, left, right)
        _quicksort(array, left, pivot_idx - 1)
        _quicksort(array, pivot_idx + 1, right)


def sort(array):
    # Efektivnejsia in-place implementacia
    _quicksort(array, 0, len(array) - 1)
    return array

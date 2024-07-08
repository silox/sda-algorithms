def binary_search(array, elem):
    left = 0
    right = len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] == elem:
            return mid
        elif elem < array[mid]:
            right = mid
        else:
            left = mid + 1

    return None


if __name__ == "__main__":
    array = [-2, 0, 3, 3, 6, 10, 50, 102]
    print(binary_search(array, 0))
    print(binary_search(array, 3))
    print(binary_search(array, 102))
    print(binary_search(array, -3))
    print(binary_search(array, 2))
    print(binary_search(array, 200))

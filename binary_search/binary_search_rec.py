def binary_search(array, elem):
    return binary_search_rec(array, elem, 0, len(array))


def binary_search_rec(array, elem, left, right):
    mid = (left + right) // 2
    if left >= right:
        return None
    if array[mid] == elem:
        return mid
    if elem < array[mid]:
        return binary_search_rec(array, elem, left, mid)

    return binary_search_rec(array, elem, mid + 1, right)


if __name__ == "__main__":
    array = [-2, 0, 3, 3, 6, 10, 50, 102]
    print(binary_search(array, 0))
    print(binary_search(array, 3))
    print(binary_search(array, 102))
    print(binary_search(array, -3))
    print(binary_search(array, 2))
    print(binary_search(array, 200))

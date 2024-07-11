import heapq


# Napis funkciu `find_k_smallest(array, k)`, ktora vrati zoznam `k` najmensich hodnot v zozname.
def find_k_smallest(array, k):
    assert 0 <= k <= len(array)
    array = array[:]
    heapq.heapify(array)
    result = []
    for _ in range(k):
        result.append(heapq.heappop(array))
    return result


def find_k_smallest_alternative(array, k):
    assert 0 <= k <= len(array)
    return heapq.nsmallest(k, array)


if __name__ == '__main__':
    array1 = [1, 2, 3, 4, 5]
    array2 = [5, 4, 3]
    array3 = [3, 0, -1, -4, 50, 3, 6, 6, 4, 19, 20]
    print(find_k_smallest(array1, 3))
    print(find_k_smallest(array2, 3))
    print(find_k_smallest(array3, 3))
    # print(find_k_smallest(array1, 10))  # Assertion Error

    print(find_k_smallest_alternative(array3, 5))
    print(array3)
    print(array1)

from collections import deque

# Napis funkciu k_window_highest(array, k), ktora vrati list
# najvacsich hodnot pre kazdu k-ticu (k cisel iducich za sebou) v
# zozname. Vysledny list bude mat teda dlzku len(array) - k + 1.
# priklad
# [-2, 5, 0, 0, -3, 4, 3], 3 ~> [5, 5, 0, 4, 4]


def k_window_highest(array, k):
    assert k <= len(array)

    window = deque(array[:k])
    result = []
    for elem in array[k:]:
        result.append(max(window))
        window.popleft()
        window.append(elem)

    return [*result, max(window)]


def k_window_highest_effective(array, k):
    result = []
    window = deque()

    for i in range(len(array)):
        if window and window[0] == i - k:
            window.popleft()

        while window and array[window[-1]] < array[i]:
            window.pop()

        window.append(i)

        if i >= k - 1:
            result.append(array[window[0]])

    return result


if __name__ == "__main__":
    array = [-2, 5, 0, 0, -3, 4, 3]
    print(k_window_highest(array, 3))
    print(k_window_highest_effective(array, 3))

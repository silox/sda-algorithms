# Task 1
# Napis funkciu sum_rec(n), ktora rekurzivne pocita sumu cisel od 1 po N pre zadane N cez parameter.

def sum_rec(n, results={0: 0}):
    if n not in results:
        results[n] = n + sum_rec(n - 1)
    return results[n]

# Task 2
# Napis rekurzivnu funkciu find_max_rec(array), ktora najde maximalny prvok v liste zadanom v parametri


def _find_max(array, idx, highest):
    if idx == -1:
        return highest

    if array[idx] > highest:
        highest = array[idx]

    return _find_max(array, idx - 1, highest)


def find_max_rec(array):
    return _find_max(array, len(array) - 1, -float('inf'))


print(sum_rec(10))
print(find_max_rec([5, -3, 20, 20, 85, -3]))
print(find_max_rec(list(range(200))))

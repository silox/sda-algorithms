# Napis funkciu bin_search_2d(array, elem), ktora ocakava usporiadany dvojrozmerny list
# cisel a vrati index (x, y) hladaneho cisla, ak sa tam cislo nachadza. V opacnom pripade None.
# Ocakavana casova zlozitost je linearna - O(n).

def bin_search_2d(array, elem):
    x = len(array) - 1
    y = 0
    while x >= 0 and y < len(array):
        if array[x][y] == elem:
            return x, y
        elif array[x][y] > elem:
            x -= 1
        elif array[x][y] < elem:
            y += 1

    return None


if __name__ == "__main__":
    array2d = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(bin_search_2d(array2d, 10))  # (1, 0)
    print(bin_search_2d(array2d, 6))  # None
    print(bin_search_2d(array2d, 60))  # None

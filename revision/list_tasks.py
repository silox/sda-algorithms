# Task 1
# Napis funkciu, ktora zoberie list cisel a zisti, ci existuju 2 cisla a, b take, ze
# b = 2 * a
# teda ze tam existuje dvojica cisel, kde jedno je dvojnasobkom druheho
# Priklad
# [2, 6, 4] ~> True
# [3, 9, 1] ~> False


def is_doubled(array):
    for i, val1 in enumerate(array):
        for j, val2 in enumerate(array):
            if i == j:
                continue
            if val1 == val2 * 2 or val1 * 2 == val2:
                return True
    return False


def is_doubled_effective(array):
    seen = set()
    for num in array:
        if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)
    return False


# Task 2
# Napis funkciu, ktora zoberie list stringov a vrati ich najdlhsi spolocny prefix.
# Priklad
# ["flower", "flow", "flight"] ~> "fl"
# ["dog", "racecar", "car"] ~> ""

def find_prefix(array):
    longest_prefix = []
    for i in range(min(len(word) for word in array)):
        char = array[0][i]
        for word in array:
            if word[i] != char:
                return ''.join(longest_prefix)
        longest_prefix.append(char)

    return ''.join(longest_prefix)


if __name__ == "__main__":
    arr0 = []
    arr1 = [2, 6, 4]
    arr2 = [3, 9, 1]
    arr3 = [1, 0]
    print(is_doubled(arr0))
    print(is_doubled(arr1))
    print(is_doubled(arr2))
    print(is_doubled(arr3))
    print()
    print(is_doubled_effective(arr0))
    print(is_doubled_effective(arr1))
    print(is_doubled_effective(arr2))
    print(is_doubled_effective(arr3))

    print()
    print(is_doubled_effective(list(range(1, 10**6, 2))))

    word_arr1 = ["flower", "flow", "flight"]
    word_arr2 = ["dog", "racecar", "car"]
    word_arr3 = ["dog", "doggo"]
    print(find_prefix(word_arr1))
    print(find_prefix(word_arr2))
    print(find_prefix(word_arr3))

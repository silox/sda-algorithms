def task1(n):
    if n <= 1:
        return n
    else:
        return task1(n - 1) + task1(n - 2)


def task2(s: str):
    if len(s) == 0:
        return s
    return task2(s[1:]) + s[0]


def task3(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and task3(s[1:-1])


def task4(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return task4(arr, target, low, mid - 1)
    else:
        return task4(arr, target, mid + 1, high)


def task5(arr, n):
    if n == 0:
        return 0
    else:
        return arr[n - 1] + task5(arr, n - 1)


def task6(n):
    if n < 10:
        return n
    else:
        return task6(n // 10)

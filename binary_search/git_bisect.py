def is_working(version):
    return version < 5


def find_bug_version(commit_history):
    left = 0
    right = len(commit_history)
    while left < right:
        mid = (left + right) // 2
        if is_working(commit_history[mid]):
            left = mid + 1
        else:
            right = mid

    return right


if __name__ == "__main__":
    ch = [0, 1, 2, 3, 4, 5, 6, 7]
    ch2 = [4, 5]
    ch3 = [5]

    print(find_bug_version(ch))
    print(find_bug_version(ch2))
    print(find_bug_version(ch3))

def get_interval_sum(array, queries):
    result = []
    for start, end in queries:
        result.append(sum(array[start:end + 1]))
    return result


def get_interval_sum_effective(array, queries):
    prefix_sums = [0]
    for value in array:
        prefix_sums.append(prefix_sums[-1] + value)

    result = []
    for start, end in queries:
        result.append(prefix_sums[end + 1] - prefix_sums[start])
    return result


if __name__ == "__main__":
    array = [1, 5, 8, 3, 0, 0, 10]
    queries = [
        (0, 0),
        (0, 4),
        (2, 2),
        (3, 5),
        (6, 6),
        (0, 6),
    ]
    print(get_interval_sum(array, queries))
    print(get_interval_sum_effective(array, queries))

    array = list(range(10**6))
    queries = [(0, 10**6 - 1)] * 10**6
    get_interval_sum_effective(array, queries)
    print('ok')

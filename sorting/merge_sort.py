def sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = sort(array[:mid])
    right = sort(array[mid:])

    return merge(left, right)


def merge(left, right):
    merged_list = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    # If there are remaining elements in the left list, add them to the merged list
    if i <= len(left):
        merged_list.extend(left[i:])

    # If there are remaining elements in the right list, add them to the merged list
    if j <= len(right):
        merged_list.extend(right[j:])

    return merged_list

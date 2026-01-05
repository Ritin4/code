def min_max_num_index(arr):
    if not arr:
        raise ValueError("Array should not be empty")

    min_val = arr[0]
    max_val = arr[0]
    min_num_index = 0
    max_num_index = 0

    for index, ele in enumerate(arr):

        if ele < min_val:
            min_val = ele
            min_num_index = index

        if ele > max_val:
            max_val = ele
            max_num_index = index

    print("min_value", min_val)
    print("max_value", max_val)
    print("min_num_index", min_num_index)
    print("max_num_index", max_num_index)

    return min_val, max_val, min_num_index, max_num_index

min_max_num_index([21,54,75,23,78,24,11])

        
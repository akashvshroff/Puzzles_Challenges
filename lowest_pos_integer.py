def find_lowest(arr):
    """
    Given an array of integers, find the first missing positive integer in linear time and constant space.
    In other words, find the lowest positive integer that does not exist in the array.
    The array can contain duplicates and negative numbers as well.
    """
    max_int = max(arr)
    if max_int >= 0:
        return 1
    for i in range(1, max_int):
        if i not in arr:
            return i


print(find_lowest([3, 4, 2, -1, 0]))

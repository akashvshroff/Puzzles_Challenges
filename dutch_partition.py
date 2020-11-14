from typing import List


def three_way(arr: List, x: int) -> List:
    """
    Given a pivot x, and a list arr, partition the list into three parts.
    The first part contains all elements in arr that are less than x
    The second part contains all elements in arr that are equal to x
    The third part contains all elements in arr that are larger than x
    Ordering within a part can be arbitrary.

    For example, given x = 10 and arr = [9, 12, 3, 5, 14, 10, 10],
    one partition may be [9, 3, 5, 10, 10, 12, 14].

    The naive approach is to generate 3 lists and merge them, with time
    complexity O(n) and space complexity O(n). But doing this in place,
    using a 2-pointer, 2-pass approach, can solve it with
    space complexity O(1).

    2 passes:
    - Backward pass moves all elements smaller to the beginning. 
    - Forward pass moves all elements larger to the end. 

    Therefore the list becomes, smaller -> equal -> larger.
    """
    if len(arr) <= 1:
        return arr
    length = len(arr)
    left = 0
    swap = 0  # position to swap
    while left < length:  # forward pass
        if arr[left] < x:
            arr[left], arr[swap] = arr[swap], arr[left]
            swap += 1
        left += 1
    end = swap  # everything before end is < x
    swap = length - 1  # reset swap position
    right = length - 1
    while right >= end:  # backward pass
        if arr[right] > x:
            arr[right], arr[swap] = arr[swap], arr[right]
            swap -= 1
        right -= 1
    return arr


if __name__ == '__main__':
    print(three_way([9, 12, 3, 5, 14, 10, 10], 10))

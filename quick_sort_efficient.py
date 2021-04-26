def quick_sort(arr, l, r):
    """
    A more memory efficient version of quick sort which uses a 2 pointer approach
    and in-place array swaps. 
    """
    if l < r:
        m1, m2 = partition(arr, l, r)
        quick_sort(arr, l, m1-1)
        quick_sort(arr, m2+1, r)


def partition(arr, left, right):
    """
    Partition step in place using a two pass approach. 
    """
    pivot = arr[left]
    swap = left

    while left <= right:
        if arr[left] < pivot:
            arr[left], arr[swap] = arr[swap], arr[left]
            swap += 1
        left += 1

    end = swap  # everything [0:end] is < pivot
    swap = right
    while right >= end:
        if arr[right] > pivot:
            arr[right], arr[swap] = arr[swap], arr[right]
            swap -= 1
        right -= 1

    m1 = end  # m1 is the position before the pivot after the forward pass
    m2 = swap  # m2 is the position after the pivot after the backward pass

    return m1, m2


arr = [23, 41, 32, 43, 1, 2, 34, 323, 4, 3, 5, 7, 86, 5, 4]
quick_sort(arr, 0, len(arr)-1)
print(arr)

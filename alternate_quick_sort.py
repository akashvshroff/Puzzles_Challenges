def quick_sort_alternate(A, l, r):
    """
    An alternate, more efficient approach to quick sort where the array is
    modified in place.
    """
    if l <= r:
        m = partition(A, l, r)
        quick_sort_alternate(A, l, m-1)
        quick_sort_alternate(A, m+1, r)


def partition(A, l, r):
    """
    Partitions the array into 2 after choosing a pivot and sorting.
    """
    x = A[l]  # first index -> pivot
    j = l
    for i in range(l+1, r+1):  # remaining elements
        if A[i] <= x:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[l], A[j] = A[j], A[l]
    return j


nums = [23, 41, 32, 43, 1, 2, 34, 323, 4, 3, 5, 7, 86, 5, 4]
quick_sort_alternate(nums, 0, len(nums)-1)
print(nums)

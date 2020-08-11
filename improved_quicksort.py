# Uses python3
import sys
import random


def quick_sort(A, l, r):
    """
    An alternate, more efficient approach to quick sort where the array is
    modified in place.
    """
    if l < r:
        m1, m2 = partition(A, l, r)
        quick_sort(A, l, m1-1)
        quick_sort(A, m2+1, r)


def partition(a, l, r):
    """
    Partitions the array into 2 after choosing a pivot and sorting. Returns 2
    index positions that mark the start and the end of the region with the pivot
    thereby accounting for non-unique integers.
    """
    x, j, t = a[l], l, r
    i = j

    while i <= t:
        if a[i] < x:
            a[j], a[i] = a[i], a[j]
            j += 1

        elif a[i] > x:
            a[t], a[i] = a[i], a[t]
            t -= 1
            i -= 1  # remain in the same i in this case
        i += 1
    return j, t


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

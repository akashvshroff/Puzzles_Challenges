def find_minimum(arr, low, high):
    """
    Suppose an array sorted in ascending order is rotated
    at some pivot unknown to you beforehand. Find the minimum
    element in O(log N) time. You may assume the array does
    not contain duplicates.

    For example, given [5, 7, 10, 3, 4], return 3
    """
    if high < low:  # if not rotated at all
        return arr[0]
    elif high == low:
        return arr[low]
    mid = int((high + low) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:  # mid+1 is the min
        return arr[mid+1]

    if mid > low and arr[mid] < arr[mid + 1]:  # mid is mis
        return arr[mid]

    if arr[high] > arr[mid]:  # if min element in the lower half or upper half
        return find_minimum(arr, low, mid - 1)
    return find_minimum(arr, mid + 1, high)


x = [5, 7, 10, 3, 4]
print(find_minimum(x, 0, len(x)-1))

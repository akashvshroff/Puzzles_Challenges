def find_max(arr, k):
    """
    Given an array of integers and a number k, where 1 <= k <= length of the
    array, compute the maximum values of each subarray of length k.
    Eg. arr = [10, 5, 2, 7, 8, 7] and k = 3, we should get [10,7,8,8].
    Do this in O(n) time and O(k) space. You can modify the input array
    in-place and you do not need to store the results. You can simply print
    them out as you compute them.
    """
    if not arr:
        return None
    if len(arr) <= k:
        return max(arr)
    res = []
    for i in range(len(arr)-k+1):
        res.append(max[arr[i:k+i]])
    return res


find_max([10, 5, 2, 7, 8, 7], 3)

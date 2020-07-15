def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if k == n:
        return nums
    if k > n:
        k = k % n
    for i in range(n-k):
        num = nums.pop(0)
        nums.append(num)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 4
rotate(nums, k)

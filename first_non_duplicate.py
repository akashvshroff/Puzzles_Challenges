def find_non_duplicate(nums):
    x = 0
    for num in nums:
        x ^= num
    return x


print(find_non_duplicate([1, 2, 1, 2, 3, 4, 3]))

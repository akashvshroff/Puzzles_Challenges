def find_duplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return num
        seen[num] = True


#print(find_duplicate([1, 2, 4, 5, 1, 3]))

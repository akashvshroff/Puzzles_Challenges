def find_duplicates(nums):
    dups = []
    seen = {}
    for num in nums:
        if num in seen and num not in dups:
            dups.append(num)
        else:
            seen[num] = True
    return dups


#print(find_duplicates([1, 1, 2, 3, 1, 2, 3, 4, 5, 6]))

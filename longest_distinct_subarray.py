def find_longest_distinct(nums: list) -> int:
    """
    Given an array of elements, return the length of the longest
    subarray where all its elements are distinct.
    For example, given the array [5, 1, 3, 5, 2, 3, 4, 1],
    return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].

    This approach is a modification of Kadane's algorithm and uses a time
    and space complexity of O(n). It loops through the numbers once and maintains
    a hash map to keep track of what has been seen.
    """
    longest = 0
    cur = 0

    seen = {}
    for num in nums:
        # print(f'num: {num}, cur: {cur}, longest: {longest}')
        # print(f'seen: {seen}')
        if seen.get(num, False):  # compare cur and longest
            if cur > longest:
                longest = cur
            cur = 0
            seen = {}
        cur += 1
        seen[num] = True
    if cur > longest:
        longest = cur
    return longest


print(find_longest_distinct([5, 1, 3, 5, 2, 3, 4, 1, 5]))

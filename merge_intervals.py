def merge_intervals(arr):
    nums = sorted(arr)
    merged = []
    if len(nums) <= 1:
        return nums
    else:
        merged.append(nums[0])
        for i in range(0, len(nums)):
            curr_begin, cur_end = merged[-1][0], merged[-1][1]
            next_begin, next_end = nums[i][0], nums[i][1]
            if cur_end >= next_begin:
                merged[-1][1] = max(cur_end, next_end)
            else:
                merged.append(nums[i])
        return merged


#print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))

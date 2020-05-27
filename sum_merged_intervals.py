def merge_intervals(arr):
    nums = sorted(arr)
    merged, s = [], 0
    if len(nums) <= 1:
        return 0 if not nums else nums[0][1]-nums[0][0]
    else:
        merged.append(list(nums[0]))
        for i in range(0, len(nums)):
            curr_begin, cur_end = merged[-1][0], merged[-1][1]
            next_begin, next_end = nums[i][0], nums[i][1]
            if cur_end >= next_begin:
                merged[-1][1] = max(cur_end, next_end)
            else:
                merged.append(list(nums[i]))
        for num in merged:
            s += num[1]-num[0]
        return s


print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))

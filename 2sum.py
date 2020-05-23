def find_pair(nums, target):
    arr = sorted(nums)
    s, sm, bg, pair = 0, 0, len(arr)-1, []
    while sm < bg:
        s = arr[sm] + arr[bg]
        if s > target:
            bg -= 1
        elif s < target:
            sm += 1
        else:
            index_1, index_2 = nums.index(arr[sm]), nums.index(arr[bg])
            pair = [index_1, index_2]
            return pair


print(find_pair([3, 2, 4], 6))

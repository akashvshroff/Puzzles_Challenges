def find_pair(nums, sum):
    s, sm, bg, pair = 0, 0, len(nums)-1, []
    while sm < bg:
        s = nums[sm] + nums[bg]
        if s > sum:
            bg -= 1
        elif s < sum:
            sm += 1
        else:
            pair.append((nums[sm], nums[bg]))
            return pair
    return False


#print(find_pair([1, 2, 4, 5], 8))

def three_sum(nums):
    nums.sort()
    sol = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        sm = i + 1
        bg = len(nums) - 1
        while sm < bg:
            sum = nums[i] + nums[sm] + nums[bg]
            if sum == 0:
                sol.append([nums[i], nums[sm], nums[bg]])
                while sm < bg and nums[sm] == nums[sm+1]:
                    sm = sm + 1
                while sm < bg and nums[bg] == nums[bg-1]:
                    bg = bg - 1
                sm += 1
                bg -= 1
            elif sum > 0:
                bg -= 1
            else:
                sm += 1
    return sol


print(three_sum([-1, 0, 1, 2, -1, -4]))

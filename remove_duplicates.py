class Solution(object):
    def removeDuplicates(self, nums):
        """
        Remove all the duplicates from a list inplace with O(i) extra memory.
        See also: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
        :type nums: List[int]
        :rtype: int
        """
        for num in range(len(nums)-1):
            i = num
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                nums.pop(i+1)

        return len(nums)

# Two Sum Problem from Leetcode
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, j in ((x, y) for x in range(len(nums)) for y in range(len(nums))):
            if i!=j and nums[i]+nums[j] == target:
                return [i,j]
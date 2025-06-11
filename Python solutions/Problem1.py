
class Solution(object):
    @staticmethod
    def twoSum(self, nums, target):
        for index0 in range(len(nums)):
            objetive = target - nums[index0]
            if objetive in nums and nums.index(objetive) != index0:
                return [index0, nums.index(objetive)]
        return []
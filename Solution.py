class Solution(object):
    def twoSum(self, nums, target):
        mapping = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in mapping:
                return [mapping[diff], index]
            mapping[num] = index

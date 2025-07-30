class Solution(object):
    def twoSum(self, nums, target):
        mapping = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in mapping:
                return [mapping[diff], index]
            mapping[num] = index

if __name__ == "__main__":
    obj = Solution()
    nums = [2, 7, 11, 15]   
    target = 9              
    result = obj.twoSum(nums, target)
    print("Result:", result)
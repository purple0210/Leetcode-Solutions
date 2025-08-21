class Solution(object):
    def removeElement(self, nums, val):
        ptr=0

        for i in range(0,len(nums)):

            if nums[i]!=val:

                nums[ptr] =nums[i]

                ptr=ptr+1
                
        return ptr

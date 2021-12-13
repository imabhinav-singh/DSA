import math

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = list()
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] >= 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
            else:
                result.append(abs(nums[i]))
        return result
        
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            else:
                max_len = max(max_len, temp)
                temp = 0
        max_len = max(max_len, temp)
        return max_len
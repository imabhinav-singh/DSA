class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        original_sum = (n*(n+1))/2
        missing_sum = 0
        for i in range(n):
            missing_sum += nums[i]
        
        return int(original_sum - missing_sum)
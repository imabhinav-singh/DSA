class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
        
    def maxSubArraySum(a,size):         
        max_so_far =a[0]
        curr_max = a[0]
        
        for i in range(1,size):
            curr_max = max(a[i], curr_max + a[i])
            max_so_far = max(max_so_far,curr_max)
            
        return max_so_far


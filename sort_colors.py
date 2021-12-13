class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c_zero, c_one, c_two = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c_zero += 1
            elif nums[i] == 1:
                c_one += 1
            else:
                c_two += 1
        
        idx = 0
        for i in range(c_zero):
            nums[idx] = 0
            idx += 1
        for i in range(c_one):
            nums[idx] = 1
            idx += 1
        for i in range(c_two):
            nums[idx] = 2
            idx += 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            prev = 0
            next = 1
            while next < len(nums):
                if nums[prev] == nums[next]:
                    nums.pop(next)
                else:
                    prev = next
                    next += 1
                #print(nums)
            return len(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        else:
            idx = 1
            next = 1
            while next < len(nums):
                if nums[next] != nums[next-1]:
                    nums[idx] = nums[next]
                    idx += 1
                next += 1
            return idx
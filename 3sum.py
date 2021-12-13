class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                elif nums[j] >= 0 and abs(nums[i]) - nums[j] < nums[j]:
                    break
                else:
                    if - (nums[i] + nums[j]) in hash.keys() and hash[-(nums[i] + nums[j])] > j:
                        res.append([nums[i], nums[j], -(nums[i] + nums[j])])
        return res
class Solution:
    def binarySearch(self, nums: List[int], num: int, start: int) -> int:
        lo, high = start, len(nums)-1
        while lo <= high:
            mid = int((lo + high)/2)
            if nums[mid] == num:
                return mid
            elif nums[mid] > num:
                high = mid - 1
            else:
                lo = mid + 1
        return -1
            
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_idx = [(nums[i], i) for i in range(len(nums))]
        nums_with_idx.sort(key = lambda x: x[0])
        nums.sort()
        for i in range(len(nums)):
            temp = self.binarySearch(nums, target - nums[i], i+1)
            if temp != -1:
                return [nums_with_idx[i][1], nums_with_idx[temp][1]]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            counter[target - nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] in counter.keys() and counter[nums[i]] != i:
                return [i, counter[nums[i]]]
        
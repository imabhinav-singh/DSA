class Solution:
    def nextMax(self, arr: List[int], index: int) -> int:
        greater_idx = []
        for i in range(len(arr)):
            if i == index:
                continue
            else:
                if arr[i] > arr[index]:
                    greater_idx.append(i)
        min_idx = 0
        for i in range(1, len(greater_idx)):
            if arr[greater_idx[min_idx]] > arr[greater_idx[i]]:
                min_idx = i
        #print(greater_idx[min_idx])
        return greater_idx[min_idx]
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = False
        for i in range(len(nums)-2, -1, -1):
            if nums[i] != max(nums[i::]):
                flag = True
                next_max_idx = i + self.nextMax(nums[i::], 0)
                temp = nums[i]
                nums[i] = nums[next_max_idx]
                nums[next_max_idx] = temp
                nums[i+1::] = sorted(nums[i+1::])
                break
        if not flag:
            nums.sort()

class Solution_2:  
    def swap(self, arr: List[int], i: int, j: int) -> None:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
    def reverse(self, arr: List[int], i: int) -> None:
        s_ptr, e_ptr = i, len(arr) -1
        while s_ptr <= e_ptr:
            self.swap(arr, s_ptr, e_ptr)
            s_ptr += 1
            e_ptr -= 1
            
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i+1)
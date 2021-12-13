class Solution:
    def merge(self, arr: List[int], temp_arr: List[int], left: int, mid: int, right: int) -> int:
        i = left
        j = mid + 1
        k = left
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= 2*arr[j]:
                i += 1
            else:
                inv_count += (mid - i + 1)
                j += 1
        
        i = left
        j = mid + 1        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                k += 1
                i += 1
            else:
                temp_arr[k] = arr[j]
                k += 1
                j += 1
        while i <= mid:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        while j <= right:
            temp_arr[k] = arr[j]
            k += 1
            j += 1
            
        for ctr in range(left, right+1):
            arr[ctr] = temp_arr[ctr]
            
        return inv_count
        
    
    def mergesort(self, arr: List[int], temp_arr: List[int], left: int, right: int) -> int:
        inv_count = 0
        if left < right:
            mid = (left + right)//2
            inv_count += self.mergesort(arr, temp_arr, left, mid)
            inv_count += self.mergesort(arr, temp_arr, mid+1, right)
            inv_count += self.merge(arr, temp_arr, left, mid, right)
        return inv_count
        
        
    def reversePairs(self, nums: List[int]) -> int:
        temp_arr = [0 for i in range(len(nums))]
        return self.mergesort(nums, temp_arr, 0, len(nums)-1)
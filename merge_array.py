class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_idx, nums2_idx = 0, 0
        temp_m = m

        while nums1_idx < temp_m and nums2_idx < n:
            if nums1[nums1_idx] <= nums2[nums2_idx]:
                nums1_idx += 1
            else:
                prev = -1
                for i in range(nums1_idx, m+n):
                    temp = prev
                    prev = nums1[i]
                    nums1[i] = temp
                nums1[nums1_idx] = nums2[nums2_idx]
                nums1_idx += 1
                nums2_idx += 1
                temp_m += 1
        
        while nums2_idx < n:
            nums1[nums1_idx] = nums2[nums2_idx]
            nums1_idx += 1
            nums2_idx += 1
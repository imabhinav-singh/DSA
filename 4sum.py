class Solution:
    def add(self, a: List[List[int]], b: List[int]) -> List[List[int]]:        
        exists = False
        for i in range(len(a)):
            if a[i][0] != b[0]:
                continue
            elif a[i][1] != b[1]:
                continue
            elif a[i][2] != b[2]:
                continue
            elif a[i][3] != b[3]:
                continue
            else:
                exists = True
                break
         
        if not exists:
            a.append(b)
            return a
        else:
            return a
        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = list()
        counter = {}
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if target - nums[i] - nums[j] in counter.keys():
                    counter[target - nums[i] - nums[j]].append([i, j])    
                else:
                    counter[target - nums[i] - nums[j]] = [[i, j]]
        
        for i in range(n):
            for j in range(i+1, n):
                if (nums[i] + nums[j]) in counter.keys():
                    for k in range(len(counter[nums[i] + nums[j]])):
                        idxs = counter[nums[i] + nums[j]][k]
                        if i in idxs or j in idxs:
                            continue
                        else:
                            temp = [nums[i], nums[j], nums[idxs[0]], nums[idxs[1]]]
                            temp.sort()
                            #print(temp, end=' ')
                            res = self.add(res, temp)
                            #print(res)
        
        return res
        
        
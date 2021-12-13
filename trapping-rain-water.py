class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0        
        peaks = [False for i in range(len(height))]
        first = last = -1
        asc, desc = True, False
        for i in range(1, len(height)):
            if height[i] < height[i-1]:
                if asc:
                    peaks[i-1] = True
                    if first == -1:
                        first = i-1
                    last = i-1
                    asc = False
                    desc = True
            elif height[i] > height[i-1]:
                asc = True
                desc = False
        if asc:
            peaks[len(height)-1] = True
            last = len(height)-1
                      
        water = 0
        i = first
        while first >= 0 and last != first and i <= last:
            j = i+1
            temp = 0
            maxp = -1
            while j <= last and height[j] < height[i]:
                temp += height[i] - height[j]
                if maxp == -1 and peaks[j]:
                    maxp = j
                elif peaks[j]:
                    if height[maxp] < height[j]:
                        maxp = j
                j += 1
            if j <= last:
                water += temp
                while not peaks[j]:
                    j += 1
                i = j
            elif maxp == -1:
                i = last+1
            else:
                for k in range(i+1, maxp):
                    if height[k] < height[maxp]:
                        water += height[maxp] - height[k]
                i = maxp
        return water           
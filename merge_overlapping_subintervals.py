class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        while True:
            #print(i)
            if i+1 >= len(intervals):
                break
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.remove(intervals[i+1])
                i -= 1
            i += 1
            #print(intervals)
        return intervals
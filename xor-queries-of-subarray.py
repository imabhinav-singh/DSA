class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [arr[0]]
        for i in range(1, len(arr)):
            xors.append(xors[i-1]^arr[i])
        
        results = []
        for i in range(len(queries)):
            if queries[i][0] == 0:
                results.append(xors[queries[i][1]])
            else:
                results.append(xors[queries[i][0]-1]^xors[queries[i][1]])
        return results
        
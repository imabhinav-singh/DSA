class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            pascal = [[1], [1,1]]
            for i in range(3, numRows+1):
                irow = [1 for j in range(i)]
                for j in range(1,i-1):
                    irow[j] = pascal[i-2][j-1] + pascal[i-2][j]
                pascal.append(irow)
            return pascal
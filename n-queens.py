import copy

class Solution:
    def block(self, n, board, i, j):
        temp = copy.deepcopy(board)
        for k in range(n):
            temp[k][j] = -1
            temp[i][k] = -1
            
        r, c = i-1, j-1
        while r >= 0 and c >= 0:
            temp[r][c] = -1
            r -= 1
            c -= 1        
        r, c = i+1, j+1
        while r < n and c < n:
            temp[r][c] = -1
            r += 1
            c += 1        
        r, c = i-1, j+1
        while r >= 0 and c < n:
            temp[r][c] = -1
            r -= 1
            c += 1        
        r, c = i+1, j-1
        while r < n and c >= 0:
            temp[r][c] = -1
            r += 1
            c -= 1       
        temp[i][j] = 1
        return temp
    
    def solveNQueensUtil(self, n, board, i):
        result = []
        for k in range(n):
            if board[i][k] != -1:
                temp = self.block(n, board, i, k)
                #print(temp)
                if i < n-1:
                    temp_r = self.solveNQueensUtil(n, temp, i+1)
                    for j in range(len(temp_r)):
                        result.append(temp_r[j])
                else:
                    result.append(temp)
        return result
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0 for i in range(n)] for j in range(n)]
        res = self.solveNQueensUtil(n, board, 0)
        #print(res)
        result = []
        for i in range(len(res)):
            temp = []
            for j in range(n):
                temp_str = ""
                for k in range(n):
                    temp_str += "Q" if res[i][j][k] == 1 else "."
                temp.append(temp_str)
            result.append(temp)
        return result

class Solution:    
    def transform(self, board, n):
        temp = []
        for i in range(n):
            temp.append("".join(board[i]))
        return temp
    
    def solveNQueensUtil(self, n, board, i, rows, cols, lefts, rights):
        result = []
        for k in range(n):
            if rows[i] != 1 and cols[k] != 1 and lefts[n-1-i+k] != 1 and rights[i+k] != 1:
                board[i][k] = "Q"
                if i < n-1:
                    rows[i] = 1 
                    cols[k] = 1 
                    lefts[n-1-i+k] = 1 
                    rights[i+k] = 1     
                    temp_r = self.solveNQueensUtil(n, board, i+1, rows, cols, lefts, rights)
                    for j in range(len(temp_r)):
                        result.append(self.transform(temp_r[j], n))
                    rows[i] = 0 
                    cols[k] = 0 
                    lefts[n-1-i+k] = 0 
                    rights[i+k] = 0
                else:
                    result.append(self.transform(board, n))
                board[i][k] = "."
        return result
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for j in range(n)]
        rows = [0 for i in range(n)]
        cols = [0 for i in range(n)]
        lefts = [0 for i in range(2*n-1)]
        rights = [0 for i in range(2*n-1)]
        
        res = self.solveNQueensUtil(n, board, 0, rows, cols, lefts, rights)
        return res
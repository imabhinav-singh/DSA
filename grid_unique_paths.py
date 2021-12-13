class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        else:
            m -= 1
            n -= 1
            if m < n:
                temp = m
                m = n
                n = temp
            res = 1.0
            for i in range(m+1, m+n+1):
                res *= i
                res /= (i-m)
            return int(res)
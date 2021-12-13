class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        value = 0
        n = len(columnTitle)
        for i in range(n):
            value += (26**(n-i-1))*(ord(columnTitle[i])-64)
        return value
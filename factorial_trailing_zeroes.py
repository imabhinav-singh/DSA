class Solution:
    def trailingZeroes(self, n: int) -> int:
        #return 0 if n == 0 else int(n/5 + self.trailingZeroes(n/5))
        count = 0
        while(n > 0):
            n /= 5
            count += n
            count = int(count)
        return count
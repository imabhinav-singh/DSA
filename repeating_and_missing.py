class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        temp = [0 for i in range(len(A))]
        a, b = -1, -1
        for i in range(len(A)):
            if temp[A[i] - 1] == 0:
                temp[A[i] - 1] = 1
            else:
                a = A[i]
        
        for i in range(len(temp)):
            if temp[i] == 0:
                b = i + 1
                break
        
        return [a, b]
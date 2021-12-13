class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        xors = [A[0]]
        xor_idx = {}
        for i in range(1, len(A)):
            xors.append(xors[i-1]^A[i])
        
        count = 0
        for i in range(len(A)):
            if xors[i]^B in xor_idx.keys():
                count += xor_idx[xors[i]^B]
            if xors[i] == B:
                count += 1
            if xors[i] in xor_idx.keys():
                xor_idx[xors[i]] += 1
            else:
                xor_idx[xors[i]] = 1

        return count
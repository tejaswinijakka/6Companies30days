class Solution:
    def findPosition(self, n , m , k):
        if (m <= n-k+1):
            return m+k-1
        m = m-(n-k+1)
        if(m%n != 0):
            return m%n
        return n
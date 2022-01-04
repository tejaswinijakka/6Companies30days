class Solution:
    def squaresInChessBoard(self, N):
         # code here
         ans = N*(N+1)*(2*N+1)//6
         return ans
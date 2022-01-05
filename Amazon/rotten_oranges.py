from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        delim = (-1,-1)
        t = 1
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 2):
                    q.append((i,j, ans))
                    grid[i][j] = 0
        
       
        while(q):
            x,y,ans = q.popleft()
            for i,j in [x-1, y], [x+1,y], [x,y-1], [x,y+1]:
                if 0 <= i < len(grid) and 0<=j<len(grid[0]) and grid[i][j] == 1:
                    q.append((i,j,ans+1))
                    grid[i][j] = 0
                
        
        if any(1 in row for row in grid):
            return -1
        else:
            return ans
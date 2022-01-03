class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1, p2 = 0,0
        n = len(nums)
        s = 0
        l = float("inf")
        while p2 < n:
            s = s+nums[p2]
            p2+=1
            while p1<n and s>=target:
                l = min(p2-p1,l)
                #print('l:',l)
                s = s-nums[p1]
                p1+=1
        if l==float("inf"):
            return 0
        return l
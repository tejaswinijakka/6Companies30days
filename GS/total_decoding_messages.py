'''
Case 1 : number of i and i-1 between 10 and 26
         dp[i] = dp[i-1]+dp[i-2]
Case 2 : number of i and i-1 greater than 26
         dp[i] = dp[i-1]
Case 3 : number of i = 0 and i-1 = 1 or i-1 = 2
         dp[i] = dp[i-2]
Case 4 : number of i = 0 and i-1>2
         return 0
'''

class Solution:
    def CountWays(self, s):
        # Code here
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1
        if s[0] == '0':
            return 0
        else:
            dp[1] = 1
        for i in range(2, len(s)+1):
             if s[i-1] == '0':
                if s[i-2] == '1' or s[i-2] == '2':
                    (dp[i]) = dp[i-2]%(1e9+7)
                else:
                    return 0
             else:
                if s[i-2] == '1' or (s[i-2] == '2' and int(s[i-1])<7):
                    (dp[i]) = dp[i-1]%(1e9+7)+(dp[i-2])%(1e9+7)
                else:
                    dp[i]+=dp[i-1]%(1e9+7)
        return int(dp[len(s)]%(1e9+7))
from collections import defaultdict
class Solution:
	def canPair(self, arr, k):
		# Code here
		if len(arr)%2 == 1:
		    return 0
		f = defaultdict(lambda: 0)
        for i in range(0, n):
            f[((arr[i] % k) + k) % k] += 1
        for i in range(0, n):
            rem = ((arr[i] % k) + k) % k
            if (2 * rem == k):
                if (f[rem] % 2 != 0):
                    return 0
            elif (rem == 0):
                if (f[rem] & 1):
                    return 0
            elif (f[rem] != f[k - rem]):
                 return 0
        return 1
class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        prod = 1
        p1, p2 = 0,0
        ans = 0
        while(p2 < n):
            prod = prod*a[p2]
            #keep moving until you make 
            #product less than k
            while prod >= k and p1 < p2:
                prod = prod//a[p1]
                p1+=1
            #when u get a sub-array whose prod is < k
            #All elements of that subarray also satisfy
            #the condition (no of contiguous subarrays)
            if prod < k:
                no_of_valid_subarrays = p2-p1+1
                ans = ans+no_of_valid_subarrays
            p2+=1
        return ans
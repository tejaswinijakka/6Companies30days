import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        Case 1 understood
        Case 2: str1 = ABABAB str2 = ABAB
        But GCD is not ABAB, but AB cuz, if we consider ABAB....the multiples of ABAB->
        (ABAB)(ABAB) = (ABABABAB) Do not makeup str1 which is ABABAB. But multiples
        of AB definitely makeup both ABABAB and ABAB. Therefore AB is the GCD.
        Case 2: By looking at it we know that GCD doesnt exist for it, therefore we check 
        with str1+str2 == str2+str1 which is LEETCODE == CODELEET, which is false. Therefore for such             
        strings we return an empty string. For stings which have a GCD, str1+str2==str2+str1 satisfies
        (cuz they would be same and would be the multiple of the gcd string) 
        '''
        if str1+str2 == str2+str1:
            st = math.gcd(len(str1), len(str2))
        else:
            return ''
        return str1[:st]
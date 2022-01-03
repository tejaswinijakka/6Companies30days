class Solution:
    def findTwoElement( self,arr, n):
        x = 0
        y = 0
        xor = 0
        for i in range(len(arr)):
            xor = xor^arr[i]
        for i in range(1, n+1):
            xor = xor^i
        s = xor&~(xor-1)
        for i in range(n):
            if arr[i]&s !=0:
                x = x^arr[i]
            else:
                y = y^arr[i]
        for i in range(1, n+1):
            if i&s != 0:
                x = x^i
            else:
                y = y^i
        cntx, cnty = 0, 0
        for i in range(n):
            if x == arr[i]:
                cntx+=1
            elif y == arr[i]:
                cnty+=1
        if cntx > 1:
            r = x
            m = y
        else:
            r = y
            m = x
        return r, m
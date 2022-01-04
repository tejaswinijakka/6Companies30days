class Solution:
    def doOverlap(self, l1, r1, l2, r2):
        #code here
        #if rectangles are side to side
        if r1[0] < l2[0] or l1[0] > r2[0]:
            return 0
        #if rectangle is top of another
        if l1[1] < r2[1] or l2[1] < r1[1]:
            return 0
        return 1
class Solution:
    def printMinNumberForPattern(ob,s):
        # code here
        #https://www.youtube.com/watch?v=GOCbsY7Arw4&t=441s
        stack = []
        result = ''
        num =  1 
        for i in range(len(s)):
            if s[i] == 'D':
                stack.append(num)
                num+=1
            else:
                stack.append(num)
                num+=1
                while(len(stack) > 0):
                    result = result+str(stack.pop())
        stack.append(num)
        while(len(stack) > 0):
            result+=str(stack.pop())
        return result
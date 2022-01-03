class Solution:
    #Reference vid : https://www.youtube.com/watch?v=Lj68VJ1wu84
	def getNthUglyNo(self,n):
		# code 
		arr = []
		arr.append(1)
		two_p = 0
		three_p = 0
		five_p = 0
		i = 0
		#Getting the next element from the ugly array itself
		while(i < n):
		    ele_2 = arr[two_p]*2
		    ele_3 = arr[three_p]*3
		    ele_5 = arr[five_p]*5
		    ele = min(ele_2, ele_3, ele_5)
		    arr.append(ele)
		    if ele == ele_2:
		        two_p+=1
		    if ele == ele_3:
		        three_p+=1
		    if ele == ele_5:
		        five_p+=1
		    i+=1
	    return arr[i-1]
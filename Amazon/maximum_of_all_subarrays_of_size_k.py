class Solution:
    '''1. Create a deque to store k elements.
    Run a loop and insert first k elements in the deque. 
    Before inserting the element, check if the element at the 
    back of the queue is smaller than the current element , if 
    it is so remove the element from the back of the deque, until 
    all elements left in the deque are greater than the current element. 
    Then insert the current element, at the back of the deque.
    Now, run a loop from k to end of the array.
    Print the front element of the deque.
    Remove the element from the front of the queue if they are 
    out of the current window.
    Insert the next element in the deque. Before inserting the 
    element, check if the element at the back of the queue is 
    smaller than the current element , if it is so remove the element 
    from the back of the deque, until all elements left in the deque 
    are greater than the current element. Then insert the current 
    element, at the back of the deque.
    Print the maximum element of the last window.'''
    def max_of_subarrays(self,arr,n,k):
        """ Deque will maintain decreasing order of values from
        front to rear in Qi, i.e., arr[Qi.front[]]
        to arr[Qi.rear()] are sorted in decreasing
        order"""
        d = deque()
        ans = []
        #   For first k elements
        for i in range(k):
            while d and arr[i]>=arr[d[-1]]  :
                d.pop()
            d.append(i)
            
        for i in range(k, n):
            ans.append(arr[d[0]])
            #Pop from front if element is not in current window
            while d and d[0]<=i-k:
                d.popleft()
            while d and arr[i]>=arr[d[-1]]:
                d.pop()
            d.append(i)
        ans.append(arr[d[0]])
        return ans
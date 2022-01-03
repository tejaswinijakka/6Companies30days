def encode(arr):
    i = 0
    n = len(arr)
    s = ''
    while(i < n-1):
        c = 1
        j=i
        while(j < n-1 and arr[j]==arr[j+1]):
            c+=1
            j+=1
        i = j+1
        s=s+arr[i-1]+str(c)
    return s
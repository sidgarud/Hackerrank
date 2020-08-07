def pairs(k, arr):
    # My code:
    # num=0
    # for i in range(n):
    #     for j in range(i+1,n):
    #         diff=abs(arr[i]-arr[j])
    #         if diff==k: num+=1
    # return num
# One liner: 
    return len(set(arr) & set([item + k for item in set(arr)]))
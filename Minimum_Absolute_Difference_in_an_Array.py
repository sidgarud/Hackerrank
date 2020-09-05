# Complete the minimumAbsoluteDifference function below.
# 6/10 code:
# def minimumAbsoluteDifference(arr):
#     diff=[]
#     for i in range(n):    
#         for j in range(i+1,n):
#             diff.append(abs(arr[j]-arr[i]))
#     return min(diff)

# 1)sort 2)consider diff between the first pair as min 3)compare all "consecutive pair min" with the one in step2 to get the least min.
def minimumAbsoluteDifference(arr):
    arr= sorted(arr)
    diff=2*10**9 # math.fabs(-10**9 - 10**9) = |-1BN-1BN|
    for i in range(1,n):
        # Instead of
        # x=abs(arr[i]-arr[i-1])
        # if diff>x: diff=x
        # do this
        diff = min(diff, arr[i] - arr[i-1])
    return diff
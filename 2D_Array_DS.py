def hourglassSum(arr):
    sums=[]
    for i in range(1,5):
        for j in range(1,5):
            sums.append(arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i][j]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1])
    return max(sums)
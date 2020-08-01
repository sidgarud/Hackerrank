def rotLeft(a, d):
    for i in range(d):
        a.append(a[0])#not a[i] here, that's wrong
        a.pop(0)#not i here, that's wrong
    return a

a=[1,2,3,4,5]
d=4
n=len(a)
print(rotLeft(a,d))

#Even easier implementation using slices that I looked up:
#def array_left_rotation(a, n, k):
#    alist = list(a)
#    b = alist[k:]+alist[:k]
#    return b

def countSwaps(a):
    # Why do we make n-1 iterations in bubble sort algorithm?
    # Because a swap requires at least two elements. So if you have 6 elements, you only need to consider 5 consecutive pairs.
    swaps=0
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swaps+=1
    print("Array is sorted in " + str(swaps) + " swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[n-1]))
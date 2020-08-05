def maximumToys(prices, k):
    # Greedy algorithm to be used
    num=0
    # for i in range(n):
    #     min_index=i
    #     for j in range(i+1,n):
    #         if prices[min_index]>prices[j]: min_index=j
    #     prices[min_index],prices[i]=prices[i],prices[min_index]
    # Array sorted using selection sort, but takes too much time, so used TimSort
    prices.sort()
    for p in prices:
        if p<k:
            k=k-p
            num+=1
    return num

def jumpingOnClouds(c):
    # Not accounting for exception where '1 1' occurs
    jumps = i = 0 
    while True: 
        if i<n-2 and (c[i+1]==1 or c[i+2]==0):
            i+=2
            jumps+=1
        elif i<n-1 and c[i+1]==0:
            i+=1
            jumps+=1
        else: break
    return jumps

# Compact and Smart Solution:
# def jumpingOnClouds(c):
    # count = i = 0 
    # while (i < n-2):
    #   i += (c[i+2] == 0) + 1
    #   count += 1
    # return count+(i==n-2)

# Recursive Solution:
# def jumpingOnClouds(c):
#     if len(c) == 1 : return 0
#     if len(c) == 2: return 0 if c[1]==1 else 1
#     if c[2]==1: 
#         return 1 + jumpingOnClouds(c[1:])
#     if c[2]==0:
#         return 1 + jumpingOnClouds(c[2:])
    
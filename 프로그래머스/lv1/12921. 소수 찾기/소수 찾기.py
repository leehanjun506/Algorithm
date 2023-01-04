import math
def solution(n):
    arr = [True for i in range(n+1)]
    arr[0] = False
    arr[1] = False
    for i in range(2,int(math.sqrt(n))+1):
        for j in range(2*i,n+1,i):
            arr[j] = False
    n = 0
    for i in arr:
        if i == True:
            n+=1
            
    return n
def binary_search(start,end,array):
    if start>end:
        return -1
    mid = (start+end)//2
    if array[mid] == mid:
        return array[mid]
    elif array[mid]>mid:
        return binary_search(start,mid-1,array)
    else:
        return binary_search(mid+1,end,array)
    
n = int(input())
array = list(map(int,input().split()))
result = binary_search(0,n-1,array)

print(result)

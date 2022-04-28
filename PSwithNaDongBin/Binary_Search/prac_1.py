import sys
sys.setrecursionlimit(10**7)
n = int(input())
array= list(map(int,input().split()))
m = int(input())
target = list(map(int,input().split()))

array.sort()

def binary_search(array,target,start,end):
    if start>end:
        return 'no'
    mid = (end+start)//2
    
    if array[mid]==target:
        return 'yes'
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else :
        return binary_search(array,target,mid+1,end)
    
for i in target:
    print(binary_search(array,i,0,n-1),end=' ')
    

#계수 정렬
n = int(input())
array = [0]*100001

for i in input().split():
    array[int(i)]=1
    
m = int(input())

x = list(map(int,input().split()))

for i in x:
    if array[i] == 1:
        print('yes',end=' ')
    else:
        print('no',end=' ')

#집합 자료형
n =int(input())
array = set(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

for i in x:
    if i in array:
        print('yes',end=' ')
    else:
        print('no',end=' ')
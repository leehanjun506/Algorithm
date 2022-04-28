n,m = list(map(int,input().split()))
height = list(map(int,input().split()))
height_max = max(height)
value = []
def binary(height,m,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    sum = 0
    for i in height:
        if i<mid:
            continue
        sum+= (i-mid)
    if sum >= m:
        value.append(mid)
        return binary(height,m,mid+1,end)
    else :
        return binary(height,m,start,mid-1)
    
print(max(value))

#답안 예시
n,m = list(map(int,input().split(' ')))
array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0
while(start<=end):
    total = 0
    mid = (start+end)//2
    for x in array:
        if x>mid:
            total += x-mid
    
    if total<m:
        end = mid-1
    else:
        result = mid #답 계속 갱신
        start = mid+1

print(result)
n,x = map(int,input().split())
arr = list(map(int,input().split()))

start = 0
max_v = 0
cnt = 0
while True:
    end = start+x-1
    if end >=n:
        break
    if start == 0:
        s = sum(arr[start:end+1])
    else:
        s = s-arr[start-1]+arr[end]
    
    if max_v == s:
        cnt+=1
    elif s>max_v:
        max_v = s
        cnt = 1
    
        
    start+=1
    
if max_v == 0:
    print('SAD')
else:
    print(max_v)
    print(cnt)
#백준 2110
n,c = map(int,input().split())
home = []
for i in range(n):
    home.append(int(input()))
    
home.sort()

start = 1
end = home[-1] - home[0]
while end>=start:
    current_val = home[0]
    count=1
    mid = (end+start)//2
    for i in range(1,len(home)):
        if home[i]-current_val>=mid:
            count+=1
            current_val = home[i]
    # print(count)
    if count < c: # 최대간격을 줄이자 mid를 줄이자
        end = mid-1
    else: # 최대간격을 넓히자 mid를 키우자
        start = mid+1
        result = mid

print(result)        
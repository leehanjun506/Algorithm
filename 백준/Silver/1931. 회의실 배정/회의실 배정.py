n = int(input()) # 회의의 수
time = [list(map(int,input().split())) for _ in range(n)]
time.sort(key = lambda x: (x[1],x[0]))
# print(time)


ans = 1
index = 0

for i in range(1,n):
    if time[index][1]<=time[i][0]:
        ans+=1
        index = i
print(ans)
'''
n = int(input())
coin = list(map(int,input().split()))
coin.sort()
possibe = [coin[0]]
for i in range(1,n):
    add = coin[i]
    poss_update= []
    poss_update.append(add)
    for i in possibe:
        poss_update.append(i+add)
    possibe += poss_update

min_value = 1
while True:
    if min_value in possibe:
        min_value+=1
    else:
        print(min_value)
        break
'''
n = int(input())
coin = list(map(int,input().split()))
coin.sort()

cnt = 1

for i in coin:
    if i > cnt:
        break
    cnt+=i

print(cnt)

# 정렬한 후 작은 수 넣을때마다 최소값 도출 해내면서 갱신하자
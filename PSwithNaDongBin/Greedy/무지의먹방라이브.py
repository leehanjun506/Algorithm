# https://programmers.co.kr/learn/courses/30/lessons/42891
import heapq

# 효율성 실패 case (내 풀이)
def mysolution(food_times, k):
    x=len(food_times)
    time = 0
    val = 0 # 장애발생 하기 전 섭취한 음식번호 
    while sum(food_times)!=0:
        y = x%len(food_times)
        if x==len(food_times):
            x=1
        else:
            x+=1
        if food_times[y]>0:
            food_times[y]-=1
        else:
            continue
        time+=1
        if time == k:
            val = y+1 # 장애발생전 섭취음식번호
            break
    if sum(food_times) == 0:
        return -1
    while(True):
        if val == len(food_times):
            if food_times[0]==0:
                val = 1
                continue
            return 1
        else:
            if food_times[val] == 0:
                val+=1
                continue
            return val+1

mysolution(list(map(int,input().split())),int(input()))

# 효율성 성공 case(내 풀이)
def solution(food_times, k):
    q = []
    remain = k
    qlen = len(food_times)
    index = 1
    for i in food_times:
        heapq.heappush(q,(i,index)) # i는 시간 index는 음식번호
        index+=1
    if k>=sum(food_times):
        return -1
    previous = 0
    while qlen*(q[0][0]-previous) <= remain:
        now = q[0][0]-previous 
        previous = heapq.heappop(q)[0]
        remain -= now*qlen
        qlen-=1
    ans = []
    for i in q:
        ans.append(i[1])
    ans.sort()
    remain %=len(ans)
    return ans[remain]
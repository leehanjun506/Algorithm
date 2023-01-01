import heapq
def solution(food_times, k):
    q = []
    remain = k
    qlen = len(food_times)
    index = 1
    length = len(food_times)
    for i in food_times:
        heapq.heappush(q,(i,index)) # i는 시간 index는 음식번호
        index+=1
    if k>=sum(food_times):
        return -1
    previous = 0 # 이전 시간
    while qlen*(q[0][0]-previous) <= remain:
        now = q[0][0]-previous #처음에 4 
        previous = heapq.heappop(q)[0]#4
        remain -= now*qlen #3
        qlen-=1
    ans = []
    for i in q:
        ans.append(i[1])
    ans.sort()
    remain %=len(ans)
    return ans[remain]
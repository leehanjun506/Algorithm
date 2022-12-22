#백준 1715
import heapq
n = int(input())
answer = 0
heap = []
for i in range(n):
    heapq.heappush(heap,int(input()))

while(True):
    if len(heap) == 1:
        print(answer)
        break
    sum = heapq.heappop(heap) + heapq.heappop(heap)
    answer+=sum
    heapq.heappush(heap,sum)
    
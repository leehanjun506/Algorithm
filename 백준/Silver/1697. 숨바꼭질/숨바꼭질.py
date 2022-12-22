from collections import deque
n,k = map(int,input().split())
array = [0]*100001
visited = [False]*100001
depth = [0]*100001
def bfs():
    q = deque()
    q.append(n)
    visited[n] = True
    while q:
        node = q.popleft()
        for i in range(3):
            if i == 0:
                x = node-1
            elif i == 1:
                x = node+1
            else:
                x = node*2
            if x>=0 and x<100001 and visited[x] == False :
                q.append(x)
                visited[x] = True
                depth[x] = depth[node] + 1
        if depth[k] != 0:
            break

bfs()
print(depth[k])
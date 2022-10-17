def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

plan = list(map(int,input().split()))
parent = [0]*(n+1)

tag = 0

for i in range(1,n+1):
    parent[i] = i

for i in range(n):
    for j in range(i,n):
        if graph[i][j] == 1:
            union_parent(parent,i+1,j+1)


for i in range(1,len(plan)):
    if find_parent(parent,plan[i-1]) != find_parent(parent,plan[i]):
        print("NO")
        tag = 1
        break

if tag == 0:
    print("YES")
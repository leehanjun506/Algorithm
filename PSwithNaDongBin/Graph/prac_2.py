#백준 1647
n,m = map(int,input().split())

def find_parent(parent,x):
    if parent[x] !=x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i
edges = []

max_result = 0
result = 0
for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        max_result = max(cost,max_result)
        result+=cost

print(result-max_result)
print(parent)
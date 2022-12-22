# 백준 2887
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

n = int(input())

parent = [0]*(n+1)
for i in range(len(parent)):
    parent[i] = i

xyz = []
for i in range(n):
    x,y,z = map(int,input().split())
    xyz.append((x,y,z,i+1))

x_list = sorted(xyz,key=lambda x:x[0])
y_list = sorted(xyz,key=lambda x:x[1])    
z_list = sorted(xyz,key=lambda x:x[2])
edges = []
for i in range(1,n):
    (x,node1,node2) = (abs(x_list[i][0]-x_list[i-1][0]),x_list[i-1][3],x_list[i][3])
    edges.append((x,node1,node2))

for i in range(1,n):
    (y,node1,node2) = (abs(y_list[i][1]-y_list[i-1][1]),y_list[i-1][3],y_list[i][3])
    edges.append((y,node1,node2))
    
for i in range(1,n):
    (z,node1,node2) = (abs(z_list[i][2]-z_list[i-1][2]),z_list[i-1][3],z_list[i][3])
    edges.append((z,node1,node2))

edges.sort()

ans = 0
for edge in edges:
    cost,node1,node2 = edge[0],edge[1],edge[2]
    if find_parent(parent,node1) != find_parent(parent,node2):
        union_parent(parent,node1,node2)
        ans+=cost
print(ans)
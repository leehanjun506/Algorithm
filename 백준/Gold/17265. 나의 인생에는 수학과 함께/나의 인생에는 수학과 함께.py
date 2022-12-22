n = int(input())


graph = [input().split() for _ in range(n)]

def operation(x,y,symbol):
    x = int(x)
    y = int(y)
    if symbol == '+':
        return x+y
    elif symbol == '-':
        return x-y
    else :
        return x*y
min_v,max_v = 5**5, -5**4
def dfs(y,x,num):
    if y == n-1 and x == n-1:
        global min_v  
        min_v = min(min_v,num)
        global max_v
        max_v = max(max_v,num)
    
    if y<n-2:
        dfs(y+2,x,operation(num,graph[y+2][x],graph[y+1][x]))
    if y<n-1 and x<n-1:
        dfs(y+1,x+1,operation(num,graph[y+1][x+1],graph[y][x+1]))
        dfs(y+1,x+1,operation(num,graph[y+1][x+1],graph[y+1][x]))
    if x<n-2:
        dfs(y,x+2,operation(num,graph[y][x+2],graph[y][x+1]))
        
dfs(0,0,int(graph[0][0]))
print(max_v,min_v)
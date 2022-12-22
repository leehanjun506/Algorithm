#백준14888
n = int(input())
a = list(map(int,input().split()))
# add,subtract,multiply,divide = map(int,input().split())
oper_num = list(map(int,input().split()))
cnt = 0
min_v = 1e9
max_v = -1e9
def oper(x,y,operator):
    if operator == 0:
        return x+y
    elif operator == 1:
        return x-y
    elif operator == 2:
        return x*y
    else:
        if x<0 and y>0:
            return -(abs(x)//y)
        return x//y
    
def dfs(cnt,val):
    global min_v
    global max_v
    if cnt == len(a)-1:
        min_v = min(min_v,val)
        max_v = max(max_v,val)
    for i in range(4):
        oper_num[i]-=1
        if oper_num[i] <0:
            oper_num[i]+=1
            continue
        dfs(cnt+1,oper(val,a[cnt+1],i))
        oper_num[i]+=1

dfs(0,a[0])
print(max_v)
print(min_v)
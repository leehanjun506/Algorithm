# 백준 3190
from collections import deque

n = int(input())
k = int(input())
apples = []
for _ in range(k):
    a,b = map(int,input().split())
    apples.append((a,b))
dir_num = int(input())
dir = []
for _ in range(dir_num):
    time,change = input().split()
    dir.append((int(time),change))
dir.sort()
cnt = 0
snake = deque()

# 위,오른쪽,아래,왼쪽
dx = [0,1,0,-1]
dy = [1,0,-1,0]
direction = ['R','D','L','U']
cnt_dir = 'R'
x,y = 1,1
val = 0
snake.append((x,y))

while(True):
    if x <1 or x>n or y<1 or y>n :
        break
    val+=1
        
    for i in range(len(direction)):
        if cnt_dir == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if (nx,ny) in snake:
        break
    
    if (nx,ny) not in apples:
        snake.popleft()
    else :
        apples.remove((nx,ny))
    
    snake.append((nx,ny))
    x = nx
    y = ny    
    if cnt == len(dir):
        continue
    if val == dir[cnt][0]:
        if cnt_dir == 'R':
            if dir[cnt][1] == 'D':
                cnt_dir = 'D'
            else:
                cnt_dir = 'U'
        
        elif cnt_dir == 'D':
            if dir[cnt][1] == 'D':
                cnt_dir = 'L'
            else:
                cnt_dir = 'R'
        
        elif cnt_dir == 'L':
            if dir[cnt][1] == 'D':
                cnt_dir = 'U'
            else:
                cnt_dir = 'D'
        
        else:
            if dir[cnt][1] == 'D':
                cnt_dir = 'R'
            else:
                cnt_dir = 'L'
        cnt+=1
print(val)
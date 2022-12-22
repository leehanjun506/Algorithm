from collections import deque

gear1 = deque([int(i) for i in input()])
gear2 = deque([int(i) for i in input()])
gear3 = deque([int(i) for i in input()])
gear4 = deque([int(i) for i in input()])
gear = [gear1,gear2,gear3,gear4]

def rotate(gear_number,dir):
    if dir == 1:
        gear[gear_number-1].rotate(1)
    else:
        gear[gear_number-1].rotate(-1)
    
def recursive(gear_number,dir):
    if gear_number == 1:
        visited[gear_number-1] = True
        if gear[gear_number-1][2] != gear[gear_number][6] and visited[gear_number] == False:
            poss[gear_number-1] = (True,dir)
            poss[gear_number] = (True,dir*-1)            
            recursive(gear_number+1,dir*-1)
    elif gear_number == 2 or gear_number == 3:
        visited[gear_number-1] = True
        
        if gear[gear_number-1][6] != gear[gear_number-2][2] and visited[gear_number-2] == False :
            poss[gear_number-1] = (True,dir)
            poss[gear_number-2] = (True,dir*-1)
            recursive(gear_number-1,dir*-1)
        
        if gear[gear_number-1][2] != gear[gear_number][6] and visited[gear_number] == False:
            poss[gear_number-1] = (True,dir)
            poss[gear_number] = (True,dir*-1)
            recursive(gear_number+1,dir*-1)
    else:
        visited[gear_number-1] = True
        if gear[gear_number-1][6] != gear[gear_number-2][2] and visited[gear_number-2] == False :
            poss[gear_number-1] = (True,dir)
            poss[gear_number-2] = (True,dir*-1)
            recursive(gear_number-1,dir*-1)

n = int(input())
for i in range(n):
    poss = [(False,0)]*4
    visited = [False]*4
    n,dir = map(int,input().split())
    poss[n-1] = (True,dir)
    recursive(n,dir)
    for j in range(4):
        if poss[j][0]:
            rotate(j+1,poss[j][1])
up = [gear1[0],gear2[0],gear3[0],gear4[0]]
ans = 0
for i in range(4):
    if up[i] == 1:
        ans += 2**i
print(ans)
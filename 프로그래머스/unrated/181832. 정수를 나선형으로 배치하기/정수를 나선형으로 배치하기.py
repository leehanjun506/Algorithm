def solution(n):
    
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    answer = [[0]*n for _ in range(n)]
    x,y = 0,0
    direction = 0
    cur = 1
    while cur<= n**2:
        answer[x][y] = cur
        cur+=1
        nx = x + move[direction][0]
        ny = y + move[direction][1]
        if nx>=n or ny>=n or answer[nx][ny] != 0:
            direction = (direction+1) % 4
            nx = x + move[direction][0]
            ny = y + move[direction][1]
        x,y = nx,ny
    
    return answer
n,m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]
max_value = -1
for i in range(n):
    for j in range(m):
        for y in range(-n,n): # 행 등차 
            for x in range(-m,m): # 열 등차
                num=''
                cx,cy = j,i
                while 0<=cy<n and 0<=cx<m:
                    if x ==0 and y==0:
                        if (int(int(matrix[i][j])**0.5)**2 - int(matrix[i][j])) == 0.0:
                            max_value = max(max_value,int(matrix[i][j]))
                        break
                    num+=matrix[cy][cx]
                    cx += x
                    cy += y
                    if (int(int(num)**0.5)**2 - int(num)) == 0.0:
                        max_value = max(max_value,int(num))
print(max_value)
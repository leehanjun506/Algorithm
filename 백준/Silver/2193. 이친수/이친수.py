n = int(input())
arr = [[0]*2 for _ in range(n)]
arr[0][0] = 0
arr[0][1] = 1

for i in range(1,n):
    for j in range(2):
        if j == 1:
            arr[i][j-1] += arr[i-1][j]
        else:
            arr[i][j], arr[i][j+1] = arr[i-1][j], arr[i-1][j]

print(arr[n-1][0]+arr[n-1][1])

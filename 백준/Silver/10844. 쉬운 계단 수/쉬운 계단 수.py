n = int(input())
arr = [[0]*10 for _ in range(n)]
for i in range(1,10):
    arr[0][i] = 1
for i in range(1,n):
    for j in range(10):
        if j == 0:
            arr[i][j] = arr[i-1][j+1]%1000000000
        elif j == 9:
            arr[i][j] = arr[i-1][j-1]%1000000000
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]%1000000000

sum = 0
for i in range(10):
    sum += arr[n-1][i]
print(sum%1000000000)
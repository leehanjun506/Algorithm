n = int(input())
arr = [[0]*10 for _ in range(n)]
for i in range(10):
    arr[0][i] = 1
    
for i in range(1,n):
    for j in range(10):
        for k in range(j+1):
            arr[i][j] += arr[i-1][k]
            arr[i][j] %= 10007

s = sum(arr[n-1])
print(s%10007)
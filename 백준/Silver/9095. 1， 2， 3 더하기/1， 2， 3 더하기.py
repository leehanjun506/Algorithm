num = int(input())
arr = [0]*11
arr[0] = 1
arr[1] = 2
arr[2] = 4

for i in range(num):
    n = int(input())
    for j in range(3,n):
        arr[j] = arr[j-1]+arr[j-2]+arr[j-3]
    print(arr[n-1])

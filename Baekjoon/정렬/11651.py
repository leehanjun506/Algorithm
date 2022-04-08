num = int(input())

array = []
for i in range(num):
    a = list(map(int,input().split()))
    array.append(a)
    # a,b = input().split()
    # a = int(a)
    # b = int(b)
    # list.append([a,b])
array.sort(key=lambda x:(x[1],x[0]))

for i in range(num):
    print(array[i][0],array[i][1])
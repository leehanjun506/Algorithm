num =int(input())

list = []

for i in range(num):
    a,b = input().split()
    a=int(a)
    b=int(b)
    list.append([a,b])
list.sort()
for i in range(num):
    print(list[i][0],list[i][1])

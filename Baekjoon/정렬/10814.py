n = int(input())

list = []
for i in range(n):
    age,name = input().split()
    age = int(age)
    list.append([age,name])

list.sort(key=lambda x : x[0])

for i in range(n):
    print(list[i][0],list[i][1])

n = int(input())

list = []
for i in range(n):
    name,kor,eng,math = input().split()
    kor,eng,math = int(kor),int(eng),int(math)
    list.append([name,kor,eng,math])

list.sort(key= lambda x: ([-x[1],x[2],-x[3],x[0]]))

for i in range(n):
    print(list[i][0])
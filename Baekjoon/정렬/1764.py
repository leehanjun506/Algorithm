n,m = map(int,input().split())
ans_list = {}
list = []
for i in range(n+m):
    list.append(input())
list.sort()
for i in list:
    if i in ans_list:
        ans_list[i] = 2
    else :
        ans_list[i] = 1


num = 0
for value in ans_list.values():
    if value == 2:
        num+=1
print(num)
for key,value in ans_list.items():
    if value == 2:
        print(key)
    

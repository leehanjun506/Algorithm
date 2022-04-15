# 내 풀이
n = int(input())

list = [list(input().split()) for _ in range(2)]

for i in range(2):
    list[i][1] = int(list[i][1])

    
# 답안예시
'''
array=[]
for i in range(n):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1])))
print(array)    
''' 
   
result = sorted(list,key=lambda x:(x[1]))

for x in result:
    print(x[0],end=" ")
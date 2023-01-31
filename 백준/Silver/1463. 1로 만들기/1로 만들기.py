num = int(input())
array = [0]*num

for i in range(0,num+1):
    array.append(0)

for i in range(2,num+1):
    array[i]=array[i-1]+1
    if i%3 == 0:
        array[i]=min(array[i//3]+1,array[i])
    if i%2 == 0:
        array[i]=min(array[i//2]+1,array[i])
    
print(array[i])

a=[]
index=1
for i in range(9):
   
    x=int(input())
    if(i==0):
        a.append(x)
        continue
    if(x>max(a)):
        index=i+1
    a.append(x)
   
                

print(max(a))
print(index)
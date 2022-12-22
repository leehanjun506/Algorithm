a = input().split('-')
if '+' in a[0]:
    val = list(map(int,a[0].split('+')))
    x = sum(val)
else:
     x = int(a[0])
for i in range(1,len(a)):
    if '+' in a[i]:
        y = list(map(int,a[i].split('+')))
        a[i] = sum(y)
    else:
        a[i] = int(a[i])        
    x -= a[i]
        
print(x)

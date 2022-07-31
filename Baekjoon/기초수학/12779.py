import math
a,b = map(int,input().split())

poss = 0

for i in range(1,b+1):
    x = i*i
    if x>b:
        break
    if x>a:
        poss+=1    
gcd = math.gcd(poss,b-a)
    
if poss == 0:
    print(0)
else:
    print(f"{poss//gcd}/{(b-a)//gcd}")
e,s,m = map(int,input().split())

x=0
y=0
z=0
year=0
while(True):
    if e==x and s==y and m==z:
        break
    year+=1
    x+=1
    if x>15:
        x=1
    y+=1
    if y>28:
        y=1
    z+=1
    if z>19:
        z=1
print(year)
    
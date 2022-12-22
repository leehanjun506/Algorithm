n,r = map(int,input().split())
comb_list = []
list_a = [i+1 for i in range(n)]
def comb(idx,x):
    if len(x) == r:
        comb_list.append(x[:])
    
    for i in range(idx,n):
        comb(i+1,x+[list_a[i]])
comb(0,[])
for i in comb_list:
    for j in i:
        print(j,end=" ")
    print("")

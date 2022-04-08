num = int(input())

ans = ['NO' for i in range(num)]
for i in range(num):
    a = input()
    st = list(a)
    ck = []
    for j in range(len(st)):
        if st[j] == ')':
            if len(ck)>0:
                ck.pop()
                ans[i]='YES'
            else :
                ans[i]='NO'
                break
        
        elif st[j] == '(':
            ck.append(1)
            if len(ck) == 0:
                ans[i] = 'YES'
        
    if len(ck)!=0:
        ans[i]='NO'
        

for i in range(len(ans)):
    print(ans[i])        
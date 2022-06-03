n = list(map(int,input()))
if int(n[0]) == 0: cnt = [1,0] 
else: cnt= [0,1]
for i in range(len(n)-1):
    if n[i] != n[i+1]: cnt[n[i+1]]+=1
print(min(cnt))
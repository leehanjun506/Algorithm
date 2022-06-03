n = list(input())
cnt = int(n[0])
for i in range(len(n)-1):
    if int(n[i])*int(n[i+1]) > int(n[i])+int(n[i+1]):
       cnt *= int(n[i+1])
    else:
        cnt += int(n[i+1])

print(cnt)
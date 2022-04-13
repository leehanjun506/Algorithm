n = int(input())
isThree = 3600
noThree = 45*15+60*15

if n<3:
    print((n+1)*noThree)
elif 3<=n<13:
    print(n*noThree+isThree)
elif n<23:
    print((n-1)*noThree+2*isThree)
else:
    print((n-2)*noThree+3*isThree)

# 답안 예시

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1

print(count)

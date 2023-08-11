# n+1 개의 i와 n개의 o 로 이루어짐
# Pn은 i o 가 교대로 나오는 문자열

n = int(input())
m = int(input())
s = input()

p = ''
for i in range(2*n+1):
    if i%2 == 0:
        p+='I'
    else:
        p+='O'
        
# Pn의 길이는 2n+1
# s의 길이는 m

answer = 0

for i in range(m):
    if s[i:i+2*n+1] == p:
        answer+=1

print(answer)
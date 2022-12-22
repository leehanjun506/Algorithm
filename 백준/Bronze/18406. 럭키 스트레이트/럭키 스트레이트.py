# 백준 18406

n = input()
length = len(n)
right = 0
left = 0

for i in range(0,len(n)//2):
    left += int(n[i])
    
for j in range(len(n)//2,len(n)):
    right += int(n[j])

if left == right:
    print('LUCKY')
else:
    print('READY')
n,h = map(int,input().split())
down = [0]*(h+1)
up = [0]*(h+1)

for i in range(n):
    if i%2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

for i in range(h-1,0,-1):
    down[i] += down[i+1]
    up[i] += up[i+1]

min_v = n
same_h = 0

for i in range(1,h+1):
    if min_v > (down[i] + up[h-i+1]):
        min_v = down[i] + up[h-i+1]
        same_h = 1
    elif min_v == (down[i] + up[h-i+1]):
        same_h+=1

print(min_v,same_h)
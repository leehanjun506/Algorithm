n = int(input())
group = 0
fear = list(map(int,input().split()))
fear.sort()
count = 0
for i in fear:
    count += 1
    if count >= i:
        group += 1
        count = 0

print(group)
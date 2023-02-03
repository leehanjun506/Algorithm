n,b = input().split()
sum = 0
n = n[::-1]

for i,v in enumerate(n):
    if v>='0' and v<='9':
        sum+=int(v)*int(b)**i
    else:
        v = ord(v)-55
        sum+=v*int(b)**i
print(sum)
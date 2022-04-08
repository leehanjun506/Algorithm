n  = input()
list = list(n)
ans = 0
num = 0
print(list)

for i in range(len(n)):
    if list[i] == '(':
        num += 1
    
    elif list[i] == ')' and list[i-1] == '(':
        num -= 1
        ans += num
    
    elif list[i] == ')':
        num -= 1
        ans += 1

print(ans)

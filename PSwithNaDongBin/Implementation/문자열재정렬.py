n = input()
number = []
str = []
for i in n:
    if i >= '1' and i <= '9':
        number.append(int(i))
    else:
        str.append(i)
num = sum(number)
str.sort()
str.append(num)
for i in str:
    print(i,end='')
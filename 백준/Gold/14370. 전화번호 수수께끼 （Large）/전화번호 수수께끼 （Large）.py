ans_array = []
n = int(input())
for i in range(n):
    number = list(input().replace(" ",""))
    ans = []
    while number:
        if 'U' in number:
            number.remove('F')
            number.remove('O')
            number.remove('U')
            number.remove('R')
            ans.append(4)

        elif 'X' in number:
            number.remove('S')
            number.remove('I')
            number.remove('X')
            ans.append(6)

        elif 'W' in number:
            number.remove('T')
            number.remove('W')
            number.remove('O')
            ans.append(2)
        elif 'G' in number:
            number.remove('E')
            number.remove('I')
            number.remove('G')
            number.remove('H')
            number.remove('T')
            ans.append(8)
        elif 'Z' in number:
            number.remove('Z')
            number.remove('E')
            number.remove('R')
            number.remove('O')
            ans.append(0)
        else:
            break
    while number:
        if 'O' in number:
            number.remove('O')
            number.remove('N')
            number.remove('E')
            ans.append(1)

        elif 'T' in number:
            number.remove('T')
            number.remove('H')
            number.remove('R')
            number.remove('E')
            number.remove('E')
            ans.append(3)

        elif 'F' in number:
            number.remove('F')
            number.remove('I')
            number.remove('V')
            number.remove('E')
            ans.append(5)
        elif 'S' in number:
            number.remove('S')
            number.remove('E')
            number.remove('V')
            number.remove('E')
            number.remove('N')
            ans.append(7)
        elif 'N' in number:
            number.remove('N')
            number.remove('I')
            number.remove('N')
            number.remove('E')
            ans.append(9)
        else:
            break
    ans.sort()
    real_ans =''
    for i in ans:
        real_ans+=str(i)
    ans_array.append(real_ans)
for i in range(n):
    print("Case #{}: {}".format(i+1,ans_array[i]))

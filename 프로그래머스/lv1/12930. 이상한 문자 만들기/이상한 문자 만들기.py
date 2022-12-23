def solution(s):
    ans = s.split(' ')
    str = ''
    for i in range(len(ans)):
        if i != 0:
            str+=' '
        for j in range(len(ans[i])):
            if (j+1)%2 == 1: #홀수
                str+=ans[i][j].upper()
            else:
                str+=ans[i][j].lower()
    return str
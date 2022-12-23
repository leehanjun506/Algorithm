def solution(n):
    x = 1
    num = 0
    while(n>=x):
        x*=3
        num+=1
    x //= 3
    if n == 1:
        return 1
    list = ""
    for _ in range(num):
        y = n//x
        n %= x
        list+=str(y)
        x //= 3
    answer = 0
    for i,v in enumerate(list):
        if i == 0:
            answer+= int(v)
        else:
            answer+= int(v)*(3**i)
    
    return answer


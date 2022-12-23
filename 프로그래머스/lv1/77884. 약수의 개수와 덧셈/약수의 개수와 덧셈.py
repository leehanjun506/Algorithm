def solution(left, right):
    l = [i for i in range(left,right+1)]
    result = 0
    def check(n,num):
        for i in range(1,n+1):
            if n%i == 0:
                num+=1
        return num
    
    for i in l:
        if check(i,0)%2 == 0:
            result+= i
        else:
            result-= i
    return result
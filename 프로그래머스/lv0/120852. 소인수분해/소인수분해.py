def solution(n):
    
    answer = set()
    d = 2
    while d <= n:
        if n%d == 0:
            n = n//d
            answer.add(d)
        else:
            d+=1
    ans = list(answer)
    ans.sort()
    return ans
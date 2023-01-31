def solution(t, p):
    answer = 0
    ans = []
    for i in range(len(t)-len(p)+1):
        ans.append(t[i:i+len(p)])
    for i in ans:
        if int(i) <= int(p):
            answer+=1
    return answer
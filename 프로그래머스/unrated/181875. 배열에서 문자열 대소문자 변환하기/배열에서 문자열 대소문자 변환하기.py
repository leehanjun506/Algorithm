def solution(strArr):
    answer = []
    for j,k in enumerate(strArr):
        s=''
        if j%2==0:
            s+=k.lower()
        else:
            s+=k.upper()
        answer.append(s)
    return answer
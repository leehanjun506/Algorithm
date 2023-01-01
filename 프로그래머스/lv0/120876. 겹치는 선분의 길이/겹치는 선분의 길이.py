def solution(lines):
    answer = 0
    dp1 = [0]*200
    dp2 = [0]*200
    dp3 = [0]*200
    for i,v in enumerate(lines):
        if i == 0:
            for j in range(v[0],v[1]):
                dp1[j+99] = 1
        if i == 1:
            for j in range(v[0],v[1]):
                dp2[j+99] = 1
        if i == 2:
            for j in range(v[0],v[1]):
                dp3[j+99] = 1
    for i in range(200):
        if dp1[i] + dp2[i] + dp3[i] > 1:
            answer+=1
    return answer
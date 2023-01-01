def solution(survey, choices):
    word = 'RTCFJMAN'
    dic = {}
    for i in word:
        dic[i] = 0
    for i in range(len(survey)):
        first = survey[i][0]
        second = survey[i][1]
        if choices[i] > 4:
            dic[second] += choices[i]-4
        else:
            dic[first] += 4-choices[i]

    print(dic)
    answer = ''

    if dic['R']>=dic['T']:
        answer+='R'
    else:
        answer+='T'
    if dic['C']>=dic['F']:
        answer+='C'
    else:
        answer+='F'
    if dic['J']>=dic['M']:
        answer+='J'
    else:
        answer+='M'
    if dic['A']>=dic['N']:
        answer+='A'
    else:
        answer+='N'
    
    return answer
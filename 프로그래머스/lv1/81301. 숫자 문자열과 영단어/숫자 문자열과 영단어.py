def solution(s):
    wton = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    answer = ''
    w = ''
    for i in s:
        if i.isdigit():
            answer+=i
        else:
            w+=i
        if w in wton.keys():
            answer+=str(wton[w])
            w = ''
    return int(answer)
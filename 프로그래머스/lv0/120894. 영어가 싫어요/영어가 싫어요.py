def solution(numbers):
    dic = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    word = ''
    ans = ''
    for i in numbers:
        word+=i
        if word in dic.keys():
            ans+=str(dic[word])
            word = ''
    return int(ans)
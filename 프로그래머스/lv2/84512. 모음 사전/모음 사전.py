def solution(word):
    val = [781,156,31,6,1]
    dic = {'A':0,'E':1,'I':2,'O':3,'U':4}
    answer = 0
    idx = 0
    for i in word:
        answer+=dic[i]*val[idx]
        idx+=1
    answer+=len(word)
    
    return answer